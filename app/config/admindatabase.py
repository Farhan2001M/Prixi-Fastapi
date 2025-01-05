import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# MongoDB Driver - use the URI from the environment variable
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URI"))

# Access the 'Prixi' database
DB = client.PrixiDB

# Access the 'AdminInfo' collection
adminlogininfo = DB.AdminInfo

#Vehicles collection
Vehiclecollection = DB.VehiclesData

# For 2nd module 
VehicleData = DB.VehicleData
