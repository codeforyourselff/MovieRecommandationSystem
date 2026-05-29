import os
import uuid
from qdrant_client import models
from src.services.fixed_chunking_service import fixed_chunking_service
from src.models.embedding_model import embedding_model
from src.services.connection_service import connection_to_cluster

class uploading_service:

    def __init__(self): 
        self.encoder = embedding_model().get_embedding()
        self.client = connection_to_cluster()
        self.batch_size = int(os.getenv("BATCH_SIZE"))

    async def upload_text(self,text,collection_name,chunking_type):
        for i in range(0,len(text),self.batch_size):
            single_chunk = text[i:i+self.batch_size]
            _points = []

            for item in single_chunk:
                if chunking_type == "fixed" and item.get("chunk"):
                    _points.append(models.PointStruct(
                        id=str(uuid.uuid4()),
                        vector={chunking_type:self.encoder.encode(item["chunk"]).tolist()},
                        payload={"text":item["chunk"],"chunking":chunking_type}
                    ))
                elif chunking_type == "sentence" and item.get("chunk"):
                    _points.append(models.PointStruct(
                        id=str(uuid.uuid4()),                                           
                        vector={chunking_type:self.encoder.encode(item["chunk"]).tolist()},
                        payload={"text":item["chunk"],"chunking":chunking_type}
                    ))  
                else:
                    _points.append(models.PointStruct(
                        id=str(uuid.uuid4()),                                           
                        vector={chunking_type:self.encoder.encode(item.text).tolist()},
                        payload={"text":item.text,"chunking":chunking_type}
                    ))
        self.client.upsert(collection_name=collection_name,points=_points)
        return {"status":201,"message":"text uploaded successfully"}
        
        
                