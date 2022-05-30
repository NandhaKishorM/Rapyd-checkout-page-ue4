import json
import boto3



def put_value(token, value,id, out,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', 'us-east-1')

    table = dynamodb.Table('CustomerID')
    response = table.put_item(
       Item={
            'token': token,
            'value': value,
               'result': {
                id:{"output":out}
                
               }
             
        }
    )
    return response


def lambda_handler(event, context):
    customerid = event['queryStringParameters']['c']
    result = event['queryStringParameters']['r']
    #customerid = "checkout_201b97ac719fc329a2b77fa8bb6e7feb"
    putvalue = put_value("token","value", customerid , result)
    response = {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps({
            "message": "Successfully put the customerid"
        })
    }
    return response
