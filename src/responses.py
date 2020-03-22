import json
from src.encoders import CustomJsonEncoder

class Response():
    """Response"""
    def __init__(self, statusCode, data):
        self.statusCode = statusCode
        self.data = data
    
    def make(self):
        response = {
            "statusCode": self.statusCode,
            "body": json.dumps(self.data, cls=CustomJsonEncoder)
        }
        return response

class SuccessResponse(Response):
    """Success Response"""
    def __init__(self, data):
        super(SuccessResponse, self).__init__(200, data)

class ErrorResponse(Response):
    """Error Response"""
    def __init__(self, data):
        super(ErrorResponse, self).__init__(400, data)