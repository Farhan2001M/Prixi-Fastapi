from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from .routes.adminRoutes import router as admin_router
from .routes.userSignupRoutes import router as signup_router
from .routes.VehicleRoutes import router as vehicle_router
from .routes.recommendationRoutes import router as recommendation
from .routes.predictionRoutes import router as prediction

app = FastAPI()

origins = ["http://localhost:3000",
           "https://localhost:3000",
           "http://localhost:3001",
           "https://localhost:3001",
           "https://prixi-admin.vercel.app",
          ]



app.include_router(admin_router)
app.include_router(signup_router)
app.include_router(vehicle_router)
app.include_router(recommendation)
app.include_router(prediction)


@app.get("/")
async def healthCheck():
  return "The haalth check is successful"
