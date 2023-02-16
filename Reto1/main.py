# FastAPI
from fastapi import FastAPI

# Routers
from api.router import router

# Kernel 
import asyncio
import sys

if sys.platform == 'win32':
    loop = asyncio.ProactorEventLoop()
    print('Windows ProactorEventLoop')
    asyncio.set_event_loop(loop)

app = FastAPI(title="CCS central API")
app.include_router(router, prefix="/api", tags=["central"])
