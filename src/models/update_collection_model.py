from pydantic import BaseModel

class update_collection_model(BaseModel):
    collection_name:str
    new_collection_name: str