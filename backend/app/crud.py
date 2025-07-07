import boto3
import uuid

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

def update_habit(habit_id, habit):
    update_expr = []
    expr_attrs = {}

    if habit.name is not None:
        update_expr.append("name = :name")
        expr_attrs[":name"] = habit.name
    if habit.completed is not None:
        update_expr.append("completed = :completed")
        expr_attrs[":completed"] = habit.completed

    if not update_expr:
        return None

    response = table.update_item(
        Key={"id": habit_id},
        UpdateExpression="SET " + ", ".join(update_expr),
        ExpressionAttributeValues=expr_attrs,
        ReturnValues="ALL_NEW",
    )
    return response["Attributes"]

def delete_habit(habit_id):
    response = table.delete_item(Key={"id": habit_id})
    return {"deleted": habit_id}
