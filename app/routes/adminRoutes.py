import motor.motor_asyncio
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any 
from pydantic import BaseModel

# Use your connection string from MongoDB Atlas
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://chfarhanilyas550:farhan123@farhan0.k7f9z.mongodb.net/Prixi?retryWrites=true&w=majority')
# Access the 'Prixi' database
DB = client.PrixiDB
#Vehicles collection
Vehiclecollection = DB.VehiclesData

router = APIRouter()

class Brand(BaseModel):
    brandName: str

@router.post("/addvehiclebrand")
async def add_vehicle_brand(brand: Brand):
    existing_brand = await Vehiclecollection.find_one({"brandName": brand.brandName})
    if existing_brand:
        raise HTTPException(status_code=400, detail="Brand already exists.")
    new_brand = {"brandName": brand.brandName,  "models": [] }
    await Vehiclecollection.insert_one(new_brand)
    return {"message": "Brand added successfully."}

@router.get("/get-car-brands")
async def get_car_brands():
    # Fetch only the `brandName` field from the Vehicles collection
    car_brands = await Vehiclecollection.find({}, {"_id": 0, "brandName": 1}).to_list(length=None)
    if not car_brands:
        raise HTTPException(status_code=404, detail="No car brands found")
    return car_brands

# Helper function to serialize the MongoDB documents 
def serialize_vehicle(vehicle: Dict[str, Any]) -> Dict[str, Any]:
    vehicle["_id"] = str(vehicle["_id"])  # Convert ObjectId to string
    return vehicle

@router.get("/vehicles", response_model=List[Dict[str, Any]])
async def get_vehicles():
    vehicles_cursor = Vehiclecollection.find()  # Get a cursor for all documents
    vehicles = await vehicles_cursor.to_list(length=None)  # Fetch all documents into a list
    return [serialize_vehicle(vehicle) for vehicle in vehicles]