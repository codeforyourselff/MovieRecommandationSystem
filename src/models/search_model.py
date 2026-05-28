from pydantic import BaseModel

class search_model(BaseModel):
    collection_name: str
    query_text: str
    stretargy: str
    top_k: int = 5


    