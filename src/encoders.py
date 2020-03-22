import json
import decimal

class CustomJsonEncoder(json.JSONEncoder):
    """
        Description:
            Decodes decimal values on json.dumps
        Links: 
            https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
    """
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(CustomJsonEncoder, self).default(o)
