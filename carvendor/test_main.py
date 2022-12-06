###################### TEST #########################
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

fake_car_data = {
    "Condition": "New",
    "Vehicle_brand": "Abarth",
    "Vehicle_model": "595",
    "Production_year": 2020,
    "Mileage_km": 1.0,
    "Power_HP": 145.0,
    "Displacement_cm3": 1400.0,
    "Fuel_type": "Gasoline",
    "Drive": "Front wheels",
    "Transmission": "Manual",
    "Type": "small_cars",
    "Colour": "gray"
}

def test_read_main():
    response = client.post("/calculate_price", json = fake_car_data)
    assert response.status_code == 200
    assert float(response.json()) == 97479.30512820513
