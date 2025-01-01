from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from .routes.adminRoutes import router as admin_routes
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient('your-mongodb-connection-string')
    app.database = app.mongodb_client["PrixiDB"]
    yield
    app.mongodb_client.close()

app = FastAPI(lifespan=lifespan)

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

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )

app.include_router(admin_routes)