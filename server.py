from fastapi import FastAPI, HTTPException
from fastapi import Path
import sqlite3
import datetime

from voucher import Voucher

app = FastAPI()

# Create database table if it doesn't exist
def create_table():
    conn = sqlite3.connect('vouchers.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data
                      (ID TEXT PRIMARY KEY,
                       voucher_limit INTEGER,
                       end_date TEXT)''')
    conn.commit()
    conn.close()

def delete_voucher(id):
    current_date = datetime.datetime.now().date()
    conn = sqlite3.connect('vouchers.db')
    cursor = conn.cursor()
    message = ""

    try:
        cursor.execute("SELECT voucher_limit, end_date FROM data WHERE ID = ?", (id,))
        row = cursor.fetchone()
        if row:
            limit, date = row
        else:
            raise HTTPException(status_code=404, detail="Voucher ID not found")

        db_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        if current_date > db_date:
            message = "Voucher expired"
        else:
            if limit > 0:
                limit -= 1
                cursor.execute("UPDATE data SET voucher_limit = ? WHERE ID = ?", (limit, id))
                conn.commit()
                message = f"Voucher redeemed successfully. Remaining limit: {limit}"
            else:
                cursor.execute("DELETE FROM data WHERE ID = ?", (id,))
                conn.commit()
                message = "Voucher redeemed successfully. Limit depleted."

        # Export data to text file after deleting
        export_to_txt()

    except Exception as e:
        message = f"Error: {str(e)}"

    finally:
        conn.close()
        return message

def export_to_txt():
    conn = sqlite3.connect('vouchers.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()
    conn.close()

    with open("database_export.txt", "w") as file:
        for row in data:
            file.write(str(row) + "\n")

@app.post("/add/")
async def add_voucher(voucher: Voucher):
    conn = sqlite3.connect('vouchers.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (ID, voucher_limit, end_date) VALUES (?, ?, ?)", (voucher.code, voucher.limit, voucher.end_date))
    conn.commit()
    conn.close()

    # Export data to text file after adding
    export_to_txt()

    return {"message": "Voucher created successfully"}

@app.get("/voucher/single/{voucher_id}")
async def redeem_single_voucher(voucher_id: str):
    result = delete_voucher(voucher_id)
    return {"message": result}

@app.get("/voucher/multiple/{voucher_id}/{redemptions}")
async def redeem_voucher(voucher_id: str , redemptions: int ):
    redeemed_count = 0
    for _ in range(redemptions):
        result = delete_voucher(voucher_id)
        if "redeemed successfully" in result:
            redeemed_count += 1
        else:
            raise HTTPException(status_code=404, detail=result)
    
    if redeemed_count > 0:
        return {"message": f"{redeemed_count} voucher(s) redeemed successfully."}
    else:
        raise HTTPException(status_code=404, detail="Failed to redeem voucher.")





   



