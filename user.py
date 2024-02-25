from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import requests

def single_redeem(id: str):
    url = f"http://127.0.0.1:8000/voucher/single/{id}"
    response = requests.get(url)
    return response.json()

def multiple_redeem(id: str, redemptions: int):
    url = f"http://127.0.0.1:8000/voucher/multiple/{id}/{redemptions}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    option = input("Do you want to do single or multiple redemption? (single/multiple)\n")
    id = input("Enter your coupon ID:\n")

    if option.lower() == "single":
        print(single_redeem(id))
    elif option.lower() == "multiple":
        number_of_redemption = int(input("Enter the number of redemptions:\n"))
        print(multiple_redeem(id, redemptions=number_of_redemption))


               
