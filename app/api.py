import logging
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from .routes.adminRoutes import router as admin_router
from .routes.userSignupRoutes import router as signup_router
from .routes.VehicleRoutes import router as vehicle_router
from .routes.recommendationRoutes import router as recommendation
from .routes.predictionRoutes import router as prediction
from .config.admindatabase import close_database  # Import the cleanup function

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)

origins = ["http://localhost:3000",
           "https://localhost:3000",
           "http://localhost:3001",
           "https://localhost:3001",
           "https://prixi-admin.vercel.app",  # Add this
          ]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.on_event("shutdown")
async def shutdown():
    # Close the MongoDB connection on shutdown
    await close_database()
    logging.debug("Application shutdown. MongoDB connection closed.")


@app.get("/")
async def healthCheck():
  return "The health check is successful"


app.include_router(admin_router)
app.include_router(signup_router)
app.include_router(vehicle_router)
app.include_router(recommendation)
app.include_router(prediction)

