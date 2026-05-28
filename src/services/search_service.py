from src.services.connection_service import connection_to_cluster
from sentence_transformers import SentenceTransformer

class search_service:
    def __init__(self):
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")

    async def search_and_compare(self,search_model):
        connection_instance = connection_to_cluster()
        find_collection = connection_instance.get_collection(search_model.collection_name)
        
        if find_collection==None:
            raise HTTPException(status_code=404,detail="Collection not found")
        
        results = connection_instance.query_points(
            collection_name=search_model.collection_name,
            query= self.encoder.encode(search_model.query_text),
            using=search_model.stretargy,
            limit=search_model.top_k
        )

        payload = []
        for i,point in enumerate(results.points,1):
            payload.append(point.payload)

        return payload