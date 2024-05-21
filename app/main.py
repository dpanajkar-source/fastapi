from fastapi import FastAPI
from app.views import addition

app = FastAPI()

app.include_router(addition.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
