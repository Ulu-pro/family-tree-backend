from fastapi import FastAPI

from routers import read

app = FastAPI()

app.include_router(read.router)
