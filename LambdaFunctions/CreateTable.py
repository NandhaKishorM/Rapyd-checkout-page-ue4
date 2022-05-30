import json
import boto3


def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', 'us-east-1')

    table = dynamodb.create_table(
        TableName='CustomerID',
        KeySchema=[
            {
                'AttributeName': 'token',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'value',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'token',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'value',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


def lambda_handler(event, context):
    create_table()
    response = {
        "statusCode": 200,
        "headers": {},
        "body": json."table created]
        }
    
    return response
