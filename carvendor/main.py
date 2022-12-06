from fastapi import FastAPI, Request
from carvendor import HeadlessCarVendor, CarData
import json

app = FastAPI()

hcv = HeadlessCarVendor()

@app.post("/calculate_price")
async def calculate_price(car_data: CarData):
    print(car_data)
    return hcv.calculate_price(car_data)