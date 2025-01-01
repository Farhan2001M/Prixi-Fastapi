import uvicorn
from app.api import app  # Import the FastAPI app from app.api

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, reload=True)
