from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_case,
    delete_case,
    retrieve_case,
    retrieve_all_cases,
    update_case,
)
from app.server.models.case import (
    ErrorResponseModel,
    ResponseModel,
    CaseSchema,
    UpdateCaseModel,
)

router = APIRouter()


@router.post("/", response_description="Case data added into the database")
async def add_case_data(case: CaseSchema = Body(...)):
    case = jsonable_encoder(case)
    new_case = await add_case(case)
    return ResponseModel(new_case, "Case added successfully.")


@router.get("/", response_description="All cases retrieved")
async def get_all_cases():
    cases = await retrieve_all_cases()
    if cases:
        return ResponseModel(cases, "All case data retrieved successfully")
    return ResponseModel(cases, "Empty list returned")


@router.get("/{id}", response_description="Case data retrieved")
async def get_case_data(id):
    case = await retrieve_case(id)
    if case:
        return ResponseModel(case, "Case data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Case doesn't exist.")


@router.put("/{id}")
async def update_case_data(id: str, req: UpdateCaseModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_case = await update_case(id, req)
    if updated_case:
        return ResponseModel(
            "Case with ID: {} name update is successful".format(id),
            "Case name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the case data.",
    )


@router.delete("/{id}", response_description="Case data deleted from the database")
async def delete_case_data(id: str):
    deleted_case = await delete_case(id)
    if deleted_case:
        return ResponseModel(
            "Case with ID: {} removed".format(
                id), "Case deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Case with id {0} doesn't exist".format(
            id)
    )
