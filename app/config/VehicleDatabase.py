import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# MongoDB Driver - use the URI from the environment variable
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URI"))

db = client.PrixiDB
collection = db.VehiclesData





# import motor.motor_asyncio

# # MongoDB Atlas connection string
# atlas_uri = "mongodb+srv://chfarhanilyas550:farhan123@prixi.4pixy.mongodb.net/"

# # Create an AsyncIOMotorClient instance to connect to Atlas
# client = motor.motor_asyncio.AsyncIOMotorClient(atlas_uri)

# # Access the 'PrixiDB' database
# db = client.prixidb

# # Access the 'Vehicles' collection
# collection = db.vehiclesinfo  # You can change this to the appropriate collection name
