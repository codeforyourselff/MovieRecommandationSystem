from src.services.connection_service import connection_to_cluster
from src.models.create_collection_model import create_collection_model
from qdrant_client import models
from fastapi import HTTPException
import http

class collection_service:
    def __init__(self):
        pass

    async def create_collection(self,create_collection_model):
        try:
            connection_service_instance = connection_to_cluster()
            connection_service_instance.create_collection(collection_name=create_collection_model.collection_name ,vectors_config={
                "fixed":models.VectorParams(size=384,distance=models.Distance.COSINE),
                "sentence":models.VectorParams(size=384,distance=models.Distance.COSINE),
                "semantic":models.VectorParams(size=384,distance=models.Distance.COSINE)
            })
            return {"status":201,"message":f"collection {create_collection_model.collection_name} created successfully"}
        except Exception as e:
            print(e)
            raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,detail={"message":"Collection creation failed","data":None})
    
    async def get_all_collections(self):
        try:
            connection_service_instance = connection_to_cluster()
            result = connection_service_instance.get_collections()
            return result.collections
        except Exception as e:
            print(e)

    async def delete_collection(self,collection_name:str):
        try:
            connection_service_instance = connection_to_cluster()
            result = connection_service_instance.delete_collection(collection_name)
            return result
        except Exception as e:
            print(e)