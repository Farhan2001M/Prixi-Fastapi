import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Importing routers
from .routes.adminRoutes import router as admin_router
from .routes.userSignupRoutes import router as signup_router
from .routes.VehicleRoutes import router as vehicle_router
from .routes.recommendationRoutes import router as recommendation
from .routes.predictionRoutes import router as prediction

app = FastAPI()

# CORS middleware setup
origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost:3001",
    "https://localhost:3001",
    "https://prixi-admin.vercel.app",
    "https://prixi.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Including routes
app.include_router(admin_router)
app.include_router(signup_router)
app.include_router(vehicle_router)
app.include_router(recommendation)
app.include_router(prediction)

# Health check route
@app.get("/")
async def healthCheck():
    return "The health check is successful"

# The main entry point for the application
if __name__ == "__main__":
    # Fetching the port from the environment variable (default to 8000)
    port = int(os.getenv('PORT', 8000))  
    uvicorn.run(app, host="0.0.0.0", port=port)
