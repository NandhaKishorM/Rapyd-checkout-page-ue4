import json
import boto3


def get_value(token,value, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', 'us-east-1')

    table = dynamodb.Table('CustomerID')

    try:
        response = table.get_item(Key={'token':token, 'value': value})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


def lambda_handler(event, context):


    customerid = event['queryStringParameters']['c']
    out = get_value("token","value")
    out = out["result"][customerid]["output"]
    out = str(out)
    

    
    
    response = {
        "statusCode": 200,
         'headers': {
       
        },
        "body": json.dumps({
                  "message": [{"coin":out}]
        })
    }
    return response
