import traceback
from typing import Union

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from url_shortner.validator import InputUrlValidator, Response, ResponseError
from url_shortner.utils.utils import Schortner, Meta


route = APIRouter(
    prefix="/api"
)

@route.post('/short_url', 
           response_model=Union[ResponseError, Response]
           )
async def make_url_shorter(data: InputUrlValidator) -> ResponseError|Response:
    
    try:
        schortner = Schortner(data.url)
        generated_url = schortner.make_url_schorter()
    
        return JSONResponse(
            status_code=200,
            content={
            'status': 'OK', 
            'msg': 'URL generated successfully', 
            'response_data': f'{generated_url}'
            }
        )
    
    except:
        return JSONResponse(
            status_code=500,
            content={
            'status': 'ERROR', 
            'msg': 'Error with url generation',
            'details': f"{traceback.format_exc()}"
            }
        )
    

@route.get('/{url_code}')
async def get_url(url_code: str):
    try:
        url = Meta().get_url(code=url_code)

        return JSONResponse(
            status_code=200,
                content={
                'status': 'OK', 
                'msg': 'URL got successfully', 
                'response_data': f'{url}'
            }
        )
    except:
            return JSONResponse(
            status_code=500,
            content={
                'status': 'ERROR', 
                'msg': 'Error with getting url',
                'details': f"{traceback.format_exc()}"
            }
        )
    