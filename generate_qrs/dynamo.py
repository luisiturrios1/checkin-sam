from ids import ids
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("checkin-CheckInTable-HPSAOI6FKOA7")

print(f"invitacion,url")
for id in ids:
    table.put_item(Item={"PK": id})
    print(f"{id},https://XXXXXXX.execute-api.us-east-1.amazonaws.com/Prod/checkin/{id}")
