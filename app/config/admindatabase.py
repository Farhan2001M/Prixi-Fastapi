import motor.motor_asyncio
import logging

# MongoDB connection string (ensure it is correct)
MONGO_URI = 'mongodb+srv://chfarhanilyas550:farhan123@farhan0.k7f9z.mongodb.net/Prixi?retryWrites=true&w=majority'

client = None  # Global variable to store the MongoDB client

# Function to get the MongoDB client and database connection
async def get_database():
    global client
    if not client:
        logging.debug("Connecting to MongoDB...")
        client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
        logging.debug("MongoDB connection established.")
    
    # Access the 'PrixiDB' database
    db = client.PrixiDB
    return db

# Ensure that connections are closed properly when the app shuts down
async def close_database():
    global client
    if client:
        logging.debug("Closing MongoDB connection...")
        client.close()
        logging.debug("MongoDB connection closed.")



# import motor.motor_asyncio

# # Use your connection string from MongoDB Atlas
# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://chfarhanilyas550:farhan123@farhan0.k7f9z.mongodb.net/Prixi?retryWrites=true&w=majority')
# # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')


# # Access the 'Prixi' database
# usersDB = client.PrixiDB

# # Access the 'AdminInfo' collection
# adminlogininfo = usersDB.AdminInfo

# #Vehicles collection
# Vehiclecollection = usersDB.VehiclesData

# # For 2nd module 
# VehicleData = usersDB.VehicleData


