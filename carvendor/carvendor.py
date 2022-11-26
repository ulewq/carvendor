import requests
from modelinterface import ModelInterface

class HeadlessCarVendor:
	def get_car_data(self):
        r=requests.post("client link")        
        return r

    def convert_data_into_dict(self, Condition, Vehicle_brand, Vehicle_model, Production_year, Mileage_km, Power_HP, Displacement_cm3
    	Fuel_type, Drive, Transmission, Type, Colour) -> dict:
    	car = {
	    'Condition': Condition,
	    'Vehicle_brand': Vehicle_brand,
	    'Vehicle_model': Vehicle_model,
	    'Production_year': Production_year,
	    'Mileage_km': Mileage_km,
	    'Power_HP': Power_HP,
	    'Displacement_cm3': Displacement_cm3,
	    'Fuel_type': Fuel_type,
	    'Drive': Drive,
	    'Transmission': Transmission,
	    'Type': Type,
	    'Colour': Colour
		}
		return car

	def calculate_price(self ,car) -> float:
		predicted_price = modelinterface.processing(car)
		return predicted_price