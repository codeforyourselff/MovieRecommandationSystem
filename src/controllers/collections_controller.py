from typing import Annotated
from src.models.create_collection_model import create_collection_model
from fastapi import APIRouter, HTTPException, Depends
from src.services.factory_service import get_collection_service
from src.services.collection_service import collection_service
import http

collection_router = APIRouter(prefix="/v1/collection",tags=["collections"],dependencies=[Depends(get_collection_service)])

#Annotation
collection_service_dependency = Annotated[collection_service,Depends(get_collection_service)]

@collection_router.post("/create_collection", status_code=http.HTTPStatus.CREATED)
async def create_collection(payload:create_collection_model,service:collection_service_dependency):
    try:
        await service.create_collection(payload)
        return JSONResponse(status_code=http.HTTPStatus.CREATED,content={"message":"Collection created successfully","data":None})
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,detail={"message":"Collection creation failed","data":None})

@collection_router.get("/collection_info/{collection_name}",status_code=http.HTTPStatus.OK)
async def get_collection_info(collection_name:str,service:collection_service_dependency):
    try:
        result = await service.get_collection_info(collection_name)
        return JSONResponse(status_code=http.HTTPStatus.OK,content={"message":"Collection info retrieved successfully","data":result})
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,detail={"message":"Collection info retrieval failed","data":None})

@collection_router.delete("/delete_collection/{collection_name}",status_code=http.HTTPStatus.OK)
async def delete_collection(collection_name:str,service:collection_service_dependency):
    try:
        await service.delete_collection(collection_name)
        return JSONResponse(status_code=http.HTTPStatus.OK,content={"message":"Collection deleted successfully","data":None})
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,detail={"message":"Collection deletion failed","data":None})