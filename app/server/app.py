from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.server.routes.student import router as StudentRouter
from app.server.routes.case import router as CaseRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")
app.include_router(CaseRouter, tags=["Case"], prefix="/case")

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
