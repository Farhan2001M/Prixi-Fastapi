from fastapi import FastAPI;

app = FastAPI()

@app.get("/")
async def healthCheck():
  return "The helath check is successful"

