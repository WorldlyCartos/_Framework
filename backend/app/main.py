from fastapi import FastAPI
from app.api.endpoints.stand_endpoint import router as stands_router

app = FastAPI()
app.include_router(stands_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
