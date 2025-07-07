import boto3
import uuid
from fastapi import HTTPException
from .models import HabitUpdate

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Habits")

def get_habits():
    response = table.scan()
    return response["Items"]

def get_habit(habit_id):
    response = table.get_item(Key={"id": habit_id})
    return response.get("Item")

def create_habit(habit):
    item = {
        "id": str(uuid.uuid4()),
        "name": habit.name,
        "completed": False,
    }
    table.put_item(Item=item)
    return item

def update_habit(habit_id: str, habit_update: HabitUpdate):
    existing = table.get_item(Key={"id": habit_id})
    if "Item" not in existing:
        raise HTTPException(status_code=404, detail="Habit not found")

    update_data = habit_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    update_fields = []
    expression_values = {}
    expression_names = {}

    for key, value in update_data.items():
        if key == "name":                       # ← reserved word
            update_fields.append("#n = :name")
            expression_names["#n"] = "name"
            expression_values[":name"] = value
        else:
            update_fields.append(f"{key} = :{key}")
            expression_values[f":{key}"] = value

    update_expression = "SET " + ", ".join(update_fields)

    try:
        response = table.update_item(
            Key={"id": habit_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
            ExpressionAttributeNames=expression_names or None,
            ReturnValues="ALL_NEW"
        )
        return response.get("Attributes")
    except Exception as e:
        print("UPDATE FAILED →", e)
        print("UpdateExpression:", update_expression)
        print("ExpressionAttributeValues:", expression_values)
        print("ExpressionAttributeNames:", expression_names)
        raise HTTPException(status_code=500, detail="Internal Server Error")




def delete_habit(habit_id):
    response = table.delete_item(Key={"id": habit_id})
    return {"deleted": habit_id}
