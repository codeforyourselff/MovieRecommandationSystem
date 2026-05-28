from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, Response
from src.services.factory_service import get_sentence_chunking_service
from src.services.sentence_chunking_service import sentence_chunking_service
from src.models.chunking_model import chunking_model
from src.services.factory_service import get_uploading_service
from src.services.uploading_service import uploading_service
import http
from fastapi.responses import JSONResponse

sentence_chunking_router = APIRouter(prefix="/v1/chunking",tags=["chunking"],dependencies=[Depends(get_sentence_chunking_service)])

#Annotation
sentence_chunking_service_dependecy = Annotated[sentence_chunking_service,Depends(get_sentence_chunking_service)]
uploading_dependecy = Annotated[uploading_service,Depends(get_uploading_service)]

@sentence_chunking_router.post("/sentence_chunking", status_code=http.HTTPStatus.CREATED)
async def sentence_chunking(payload:chunking_model,service:sentence_chunking_service_dependecy,uploading_service:uploading_dependecy):
    try:
        data = await service.sentence_chunking(payload.text)
        await uploading_service.upload_text(data,payload.collection_name,"sentence")    
        return JSONResponse(status_code=http.HTTPStatus.CREATED,content={"message":"Data processed successfully","data":data})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,detail=str(e))