import uuid
from qdrant_client import models
from src.services.fixed_chunking_service import fixed_chunking_service
from src.models.embedding_model import embedding_model
from src.services.connection_service import connection_to_cluster

class uploading_service:

    def __init__(self): 
        self._points = []
        self.encoder = embedding_model().get_embedding()
        self.client = connection_to_cluster()

    async def upload_text(self,text,collection_name):
        idx = 0
        for i in text:
            for j in i:
                self._points.append(models.PointStruct(
                    id=idx,
                    vector={"fixed":self.encoder.encode(j).tolist()},
                    payload={"text":j,"chunking":"fixed"}
                ))
                idx+=1
            
        self.client.upsert(collection_name=collection_name,points=self._points,wait=True)
        return {"status":201,"message":"text uploaded successfully"}
        
        
                