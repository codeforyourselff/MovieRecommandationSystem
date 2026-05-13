from pydantic import BaseModel

class chunking_model(BaseModel):
    text : list[dict]
    collection_name : str
