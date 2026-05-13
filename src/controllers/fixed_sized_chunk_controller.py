from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from src.services.factory_service import get_fixed_chunking_service
from src.services.fixed_chunking_service import fixed_chunking_service
from src.models.chunking_model import chunking_model
from src.services.uploading_service import uploading_service
from src.services.factory_service import get_uploading_service
import http 

fixed_chunking_router = APIRouter(prefix="/v1/chunking",tags=["chunking"],dependencies=[Depends(get_fixed_chunking_service),Depends(get_uploading_service)])

#Annotation
fixed_chunking_service_dependecy = Annotated[fixed_chunking_service,Depends(get_fixed_chunking_service)]
uploading_dependecy = Annotated[uploading_service,Depends(get_uploading_service)]


@fixed_chunking_router.post("/fixed_size_chunks", status_code=http.HTTPStatus.CREATED)
async def fixed_chunking_size(payload:chunking_model,service:fixed_chunking_service_dependecy,uploading_service:uploading_dependecy):
    try:
        chunk_ready_to_upload = []
        for each_description in payload.text:
            if each_description["description"]:
                description = each_description["description"]
                chunk_ready_to_upload.append(await service.fixed_size_chunks(description))

        await uploading_service.upload_text(chunk_ready_to_upload)
        return JSONResponse(status_code=http.HTTPStatus.CREATED,content={"message":"Data processed successfully","data":None})
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,detail={"message":"Data processing failed","data":None})