from ..models.adminmodel import Brand , BrandModel 
from ..config.admindatabase import Vehiclecollection

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any , Optional


from fastapi import APIRouter
router = APIRouter()


@router.get('/')
async def home():
    return {'msg': 'Welcome in my Admin Routes '} 

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

@router.get("/getBrandData/{brand_name}", response_model=Optional[BrandModel])
async def get_vehicle_brand(brand_name: str):
    brand_data = await Vehiclecollection.find_one({"brandName": brand_name})
    if brand_data is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    # Convert ObjectId to string for JSON serialization
    brand_data["_id"] = str(brand_data["_id"])
    # Ensure models is a valid list
    if "models" not in brand_data:
        brand_data["models"] = []
    return brand_data
