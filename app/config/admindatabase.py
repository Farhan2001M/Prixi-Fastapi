import motor.motor_asyncio

# Use your connection string from MongoDB Atlas
# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://chfarhanilyas550:farhan123@farhan0.k7f9z.mongodb.net/Prixi?retryWrites=true&w=majority')
# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb+srv://chfarhanilyas550:farhan123@farhan0.k7f9z.mongodb.net/Prixi?retryWrites=true&w=majority',
    serverSelectionTimeoutMS=5000  # Timeout after 5 seconds if unable to connect
)
# Access the 'Prixi' database
usersDB = client.PrixiDB

#Vehicles collection
Vehiclecollection = usersDB.VehiclesData

# Access the 'AdminInfo' collection
adminlogininfo = usersDB.AdminInfo


# For 2nd module 
VehicleData = usersDB.VehicleData
