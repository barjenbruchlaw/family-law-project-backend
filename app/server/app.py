from fastapi import FastAPI

from app.server.routes.student import router as StudentRouter
from app.server.routes.case import router as CaseRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")
app.include_router(CaseRouter, tags=["Case"], prefix="/case")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
