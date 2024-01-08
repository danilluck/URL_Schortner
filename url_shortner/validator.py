from pydantic import BaseModel

class InputUrlValidator(BaseModel):
    url: str

class Response(BaseModel):
    status: str 
    msg: str
    response_data: str
    
class ResponseError(BaseModel):
    status: str 
    msg: str
    details: str