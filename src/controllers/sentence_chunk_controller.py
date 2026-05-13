from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, Response
from src.services.factory_service import get_sentence_chunking_service
from src.services.sentence_chunking_service import sentence_chunking_service
from src.models.chunking_model import chunking_model
import http

sentence_chunking_router = APIRouter(prefix="/v1/chunking",tags=["chunking"],dependencies=[Depends(get_sentence_chunking_service)])

#Annotation
sentence_chunking_service_dependecy = Annotated[sentence_chunking_service,Depends(get_sentence_chunking_service)]

@sentence_chunking_router.post("/sentence_chunks", status_code=http.HTTPStatus.CREATED)
async def sentence_chunking(payload:chunking_model,service:sentence_chunking_service_dependecy):
    try:
        data = await service.sentence_chunking(payload.text)
        return Response(status_code=http.HTTPStatus.CREATED,content={"message":"Data processed successfully","data":data})
    except Exception as e:
        return Response(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,content={"message":"Data processing failed","data":None})