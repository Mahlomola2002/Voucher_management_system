from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import requests
import secrets
import string

class Voucher(BaseModel):
    code: str
    limit: int
    end_date: str  # Change type to string

BASE_URL = "http://127.0.0.1:8000"

#generate unique ID with length of 10
def generate_unique_id(length=10):
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        yield code

def add_voucher(voucher: Voucher):
    voucher_dict = voucher.dict()
     
    response = requests.post("http://127.0.0.1:8000/add", json=voucher_dict)
    
    return response.json()

if __name__ == "__main__":
    while True:
        user_input = input("Do you want to create a voucher ?(Yes or No)\n")
        if user_input.lower() == "no":
            break
        else:
            id_gen = generate_unique_id()
            id = next(id_gen)
            print(id)
            end_date_1 = str(input("Enter the expiring date: (yyyy-mm-dd)\n"))
            limit_1 = int(input("Enter the limit:\n"))
            voucher = Voucher(code=id, limit=limit_1, end_date=end_date_1)
            print(add_voucher(voucher))



    
