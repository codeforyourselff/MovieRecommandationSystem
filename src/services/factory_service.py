from fastapi import Request, Depends
from src.services.collection_service import collection_service
from src.services.fixed_chunking_service import fixed_chunking_service
from src.services.sentence_chunking_service import sentence_chunking_service
from src.services.semantic_service import semantic_chunking_service
from src.services.uploading_service import uploading_service
from src.services.search_service import search_service

async def get_collection_service(request:Request) -> collection_service:
    if not hasattr(request.state, "collection_service"):
        request.state.collection_service= collection_service()
    return request.state.collection_service

async def get_fixed_chunking_service(request:Request):
    if not hasattr(request.state, "fixed_chunking_service"):
        request.state.fixed_chunking_service=fixed_chunking_service()
    return request.state.fixed_chunking_service

async def get_sentence_chunking_service(request:Request):
    if not hasattr(request.state, "sentence_chunking_service"):
        request.state.sentence_chunking_service=sentence_chunking_service()
    return request.state.sentence_chunking_service

async def get_semantic_chunking_service(request:Request):
    if not hasattr(request.state, "semantic_chunking_service"):
        request.state.semantic_chunking_service=semantic_chunking_service()
    return request.state.semantic_chunking_service

async def get_uploading_service(request:Request):
    if not hasattr(request.state, "uploading_service"):
        request.state.uploading_service=uploading_service()
    return request.state.uploading_service

async def get_search_service(request:Request):
    if not hasattr(request.state, "search_service"):
        request.state.search_service=search_service()
    return request.state.search_service
