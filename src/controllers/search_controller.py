import http
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from src.services.factory_service import get_search_service
from src.models.search_model import search_model
from src.services.search_service import search_service
from fastapi.responses import JSONResponse

searching_router = APIRouter(prefix="/v1/search",tags=["search"])

# Annotation
search_service_dependecy = Annotated[search_service,Depends(get_search_service)]

@searching_router.post("/search_and_compare",status_code=http.HTTPStatus.OK)
async def search_and_compare(search_model:search_model,service:search_service_dependecy):
    try:
        data = await service.search_and_compare(search_model)
        return JSONResponse(status_code=http.HTTPStatus.OK,content={"message":"Data processed successfully","data":data})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,detail=str(e))