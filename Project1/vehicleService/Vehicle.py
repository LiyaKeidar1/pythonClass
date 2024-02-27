

from fastapi import FastAPI
from pydantic import BaseModel
import requests

from Visa import payment


app = FastAPI()
# uvicorn Vehicle:app --host 0.0.0.0 --port 8000

class Vehicle(BaseModel):
    company: str
    model: str
    license_plate: int
    color: str
    engine: str
    mileage: float
    current_owner: str
    price: float

vehicles = {
    54321: {
        "company": "Ford",
         "model": "Mustang",
        "license_plate": 54321,
        "color": "Yellow",
        "engine": "V8",
        "mileage": 25000.8,
        "current_owner": "Robert Johnson",
        "price": 30000.0
    },
    67890:{
    "company": "Honda",
    "model": "Civic",
    "license_plate": 67890,
    "color": "Red",
    "engine": "Inline-4",
    "mileage": 35000.2,
    "current_owner": "Jane Smith",
    "price": 18000.0
},
    12345 :{
    "company": "Toyota",
    "model": "Camry",
    "license_plate": 12345,
    "color": "Blue",
    "engine": "V6",
    "mileage": 50000.5,
    "current_owner": "John Doe",
    "price": 20000.0
}
}
# vehicles1={}

# with open("./cars.json", "r") as cars:
#     my_cars= json.load(cars)
# #
# for item in my_cars.items():
#     vehicles1[item[0]]= Vehicle(**item[1])

@app.post("/vehicles/")
async def create_vehicle(vehicle: Vehicle):
    vehicles[vehicle.license_plate]=vehicle
    return vehicle

@app.get("/vehicle/{license_num}")
async def get_vehicle(license_num: int):
   return vehicles.get(license_num,"No such vehicle")


@app.put("/vehicle_update/{new_mileage}")
async def update_milage(license_plate: int, new_mileage: float):
    vehicles[license_plate]["mileage"]= new_mileage
    return vehicles[license_plate]

@app.post("/Vehicles/buy/")
async def buy_vehicle_with_visa(license_plate_id: int, card_number: int):
    VISAURL = "http://127.0.0.1:8001/run_transaction/"  # Update with your Visa module URL
    p=payment(costumer="Liya's Factory", card_number= card_number, price=vehicles[license_plate_id]["price"])

    response = requests.post(url=VISAURL, data=p.model_dump_json())
    if response.status_code<300:
        if response.json().get("approved"):
            del vehicles[license_plate_id]
        return  response.json()
    else:
        return  {"message":"Huston we have"}



# if __name__=="__main__":
#     my_port = int(os.getenv("PORT"))
#     uvicorn.run(app, host="0.0.0.0", port=my_port)
