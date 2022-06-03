from typing import Optional

from pydantic import BaseModel, Field


class CaseSchema(BaseModel):
    clientName: str = Field(...)
    respondName: str = Field(...)
    caseNumber: str = Field(...)
    caseType: str = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "clientName": "Mary Roe",
                "respondName": "John Doe",
                "caseNumber": "22XX-FC000000",
                "caseType": "Marriage Dissolution",                
            }
        }


class UpdateCaseModel(BaseModel):
    clientName: Optional[str]
    respondName: Optional[str]
    caseNumber: Optional[str]
    caseType: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "clientName": "Mary Roe",
                "respondName": "John Doe",
                "caseNumber": "22XX-FC000000",
                "caseType": "Marriage Dissolution",                
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
