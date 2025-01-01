import motor.motor_asyncio

# Use your connection string from MongoDB Atlas
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://chfarhanilyas550:farhan123@farhan0.k7f9z.mongodb.net/Prixi?retryWrites=true&w=majority')

# Access the 'Prixi' database
DB = client.PrixiDB

#Vehicles collection
Vehiclecollection = DB.VehiclesData

