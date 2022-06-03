import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

database2 = client.cases

student_collection = database.get_collection("students_collection")

case_collection = database2.get_collection("cases_collection")

# helpers


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }

# Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from the database
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True

def case_helper(case) -> dict:
    return {
        "id": str(case["_id"]),
        "clientName": case["clientName"],
        "respondName": case["respondName"],
        "caseNumber": case["caseNumber"],
        "caseType": case["caseType"],
    }
# Retrieve all cases present in the database
async def retrieve_all_cases():
    cases = []
    async for case in case_collection.find():
        cases.append(case_helper(case))
    return cases


# Add a new case into to the database
async def add_case(case_data: dict) -> dict:
    case = await case_collection.insert_one(case_data)
    new_case = await case_collection.find_one({"_id": case.inserted_id})
    return case_helper(new_case)


# Retrieve a case with a matching ID
async def retrieve_case(id: str) -> dict:
    case = await case_collection.find_one({"_id": ObjectId(id)})
    if case:
        return case_helper(case)


# Update a case with a matching ID
async def update_case(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    case = await case_collection.find_one({"_id": ObjectId(id)})
    if case:
        updated_case = await case_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_case:
            return True
        return False


# Delete a student from the database
async def delete_case(id: str):
    case = await case_collection.find_one({"_id": ObjectId(id)})
    if case:
        await case_collection.delete_one({"_id": ObjectId(id)})
        return True
