import requests
import json
from ModelInterface import ModelInterface
from pydantic import BaseModel

md = ModelInterface()

class CarData(BaseModel):
	Condition : str 
	Vehicle_brand: str
	Vehicle_model: str
	Production_year: int
	Mileage_km: float
	Power_HP: float
	Displacement_cm3: float
	Fuel_type:str
	Drive:str
	Transmission:str
	Type:str
	Colour:str

class HeadlessCarVendor:

	def convert_data_into_dict(self, car_data) -> dict:
		car = {
		"Condition": car_data.Condition,
		"Vehicle_brand": car_data.Vehicle_brand,
		"Vehicle_model": car_data.Vehicle_model,
		"Production_year": car_data.Production_year,
		"Mileage_km": car_data.Mileage_km,
		"Power_HP": car_data.Power_HP,
		"Displacement_cm3": car_data.Displacement_cm3,
		"Fuel_type": car_data.Fuel_type,
		"Drive": car_data.Drive,
		"Transmission": car_data.Transmission,
		"Type": car_data.Type,
		"Colour": car_data.Colour}
		return car

	def calculate_price(self ,car_data) -> float:
		car_dict = self.convert_data_into_dict(car_data)
		predicted_price = md.processing(car_dict)
		return predicted_price