import http
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from src.services.factory_service import get_semantic_chunking_service
from src.services.semantic_service import semantic_chunking_service
from src.models.chunking_model import chunking_model
from src.services.factory_service import get_uploading_service
from src.services.uploading_service import uploading_service

semantic_chunking_router = APIRouter(prefix="/v1/chunking",tags=["chunking"],dependencies=[Depends(get_semantic_chunking_service)])

#Annotation
semantic_chunking_service_dependecy = Annotated[semantic_chunking_service,Depends(get_semantic_chunking_service)]
uploading_dependecy = Annotated[uploading_service,Depends(get_uploading_service)]

@semantic_chunking_router.post("/semantic_chunking", status_code=http.HTTPStatus.CREATED)
async def semantic_chunking(payload:chunking_model,service:semantic_chunking_service_dependecy,uploading_service:uploading_dependecy):
    try:
        data = await service.semantic_chunking(payload.text)
        await uploading_service.upload_text(data,payload.collection_name)
        return JSONResponse(status_code=http.HTTPStatus.CREATED,content={"message":"Data processed successfully","data":data})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,detail=str(e))
