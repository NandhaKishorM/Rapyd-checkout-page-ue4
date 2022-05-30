import json
import boto3



    
#update the dynamodb database
def update(token, value, customerid,result, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', 'us-east-1')

    table = dynamodb.Table('CustomerID')
    val = {"output":result}
    response = table.update_item(
        Key={
            'token': token,
            'value': value
        },
              UpdateExpression='SET #attr1.#attr2= :val1',
    ExpressionAttributeNames={
            '#attr1': "result",
            '#attr2':customerid

        },
         ExpressionAttributeValues={':val1': val},
          ReturnValues='UPDATED_NEW'
    )
    return response

def lambda_handler(event, context):
    customerid= event['queryStringParameters']['c']
    result = event['queryStringParameters']['r']
 
    out = update("token","value",customerid,result)
   
   
    '''responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(output)
    return responseObject'''
    
    
    response = {
        "statusCode": 200,
          'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps({
             "message": "the result updated"
        })
    }
    return response
