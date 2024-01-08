from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

import uvicorn
from dotenv import dotenv_values

from url_shortner import app

config = dotenv_values('config.env')

api_app = FastAPI(
    swagger_ui_parameters={
        "url": f"{config['host']}/openapi.json",
        "swagger": "2.0",
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "requestSnippetsEnabled": True,
    })


api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def custom_openapi():
    if api_app.openapi_schema:
        return api_app.openapi_schema 
    openapi_schema = get_openapi(
        title="URL",
        version='0.0.1',
        routes=api_app.routes,
        servers=[
        {"url": f"{config['host']}"},
    ])

    for method in openapi_schema["paths"]:
        try:
            del openapi_schema["paths"][method]["post"]["responses"]["422"]
            del openapi_schema["paths"][method]["get"]["responses"]["422"]
            del openapi_schema["paths"][method]["delete"]["responses"]["422"]
        except KeyError:
            pass

    api_app.openapi_schema = openapi_schema
    return api_app.openapi_schema

api_app.include_router(app.route)


api_app.openapi = custom_openapi

if __name__ == '__main__':
    uvicorn.run(
        "main:api_app",
        host='0.0.0.0', 
        port=8080,
        reload=True)
    
    
        