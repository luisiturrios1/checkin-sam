import os
import boto3
import datetime
import pytz
import pystache

CHECK_IN_TABLE_NAME = os.getenv("CHECK_IN_TABLE_NAME")


def lambda_handler(event, context):

    invitacion_uuid = event["pathParameters"]["uuid"]
    current_dir = os.path.dirname(os.path.abspath(__file__))

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(CHECK_IN_TABLE_NAME)

    response = table.query(
        KeyConditionExpression="PK = :pk",
        ExpressionAttributeValues={":pk": invitacion_uuid},
    )

    if response["Count"] != 1:

        template = open(os.path.join(current_dir, "no_encontrada.html"), "r").read()
        html = pystache.render(template, {"invitacion_uuid": invitacion_uuid})
        return {
            "statusCode": 200,
            "body": html,
            "headers": {
                "Content-Type": "text/html",
            },
        }

    invitacion = response["Items"][0]

    if "checkin_date" in invitacion:
        template = open(os.path.join(current_dir, "redimida.html"), "r").read()
        html = pystache.render(template, invitacion)
        return {
            "statusCode": 200,
            "body": html,
            "headers": {
                "Content-Type": "text/html",
            },
        }

    table.put_item(
        Item={
            "PK": invitacion_uuid,
            "checkin_date": datetime.datetime.now(
                pytz.timezone("America/Mexico_City")
            ).strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

    template = open(os.path.join(current_dir, "bienvenido.html"), "r").read()
    html = pystache.render(template, invitacion)
    return {
        "statusCode": 200,
        "body": html,
        "headers": {
            "Content-Type": "text/html",
        },
    }
