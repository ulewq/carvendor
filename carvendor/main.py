from fastapi import FastAPI
from carvendor import HeadlessCarVendor

app = FastAPI()

hcv = HeadlessCarVendor()


@app.get("/get_data")
async def get_data():
    data = hcv.get_car_data()


@app.post("/get_price")
async def predicted_price():
    return hcv.calculate_price()
