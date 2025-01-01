from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from .routes.adminRoutes import router as admin_router

app = FastAPI()

origins = ["http://localhost:3000", "https://localhost:3000"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
async def healthCheck():
  return "The health check is successful"

app.include_router(admin_router)