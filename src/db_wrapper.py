import boto3
from time import strftime, time

class DBWrapper():
    """DB Wrapper"""

    def __init__(self, table):
        
        self.table = table
        self.db = boto3.resource('dynamodb').Table(table)

    def put(self, item):
        
        result = self.db.put_item(Item = item)
        return result

    def get(self, key, defaults = None, key_field = 'id'):
        
        item = defaults
        result = self.db.get_item(Key={key_field: key})

        if 'Item' in result:
            item = result['Item']

        return item

    def generate_timestamp():
        
        response = strftime("%Y-%m-%dT%H:%M:%S")
        return response
