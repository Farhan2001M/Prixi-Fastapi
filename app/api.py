from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request
from .routes.adminRoutes import router as admin_router
from .routes.userSignupRoutes import router as signup_router
from .routes.VehicleRoutes import router as vehicle_router
from .routes.recommendationRoutes import router as recommendation
from .routes.predictionRoutes import router as prediction
from ..app.config.admindatabase import usersDB

app = FastAPI()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )


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

@app.get("/db-health")
async def db_health_check():
    try:
        # Run a test query to confirm database connectivity
        await usersDB.command("ping")
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

app.include_router(admin_router)
app.include_router(signup_router)
app.include_router(vehicle_router)
app.include_router(recommendation)
app.include_router(prediction)


@app.get("/")
async def healthCheck():
  return "The helath check is successful"