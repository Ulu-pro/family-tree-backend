from fastapi import FastAPI

from routers import create, read, update, delete

app = FastAPI()

app.include_router(create.router)
app.include_router(read.router)
app.include_router(update.router)
app.include_router(delete.router)
