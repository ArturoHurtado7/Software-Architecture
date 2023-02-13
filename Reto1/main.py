# FastAPI
from fastapi import FastAPI

# Routers
from api.router import router

app = FastAPI(title="CCS central API")
app.include_router(router, prefix="/api", tags=["central"])