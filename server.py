import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
from src.controllers.collections_controller import collection_router
from src.controllers.fixed_sized_chunk_controller import fixed_chunking_router
from src.controllers.sentence_chunk_controller import sentence_chunking_router
from src.controllers.semantic_chunk_controller import semantic_chunking_router
from src.controllers.search_controller import searching_router

app = FastAPI()
router = APIRouter(prefix="/mrc",tags=[""])

@app.get("/")
async def root():
    return {"Welcome to the movie recommandation system"}

app.include_router(router)
# CRUD for collectin
app.include_router(collection_router)
# Fixed chuning type 
app.include_router(fixed_chunking_router)
# Sentence chunking type
app.include_router(sentence_chunking_router)
# Semantic chunking type
app.include_router(semantic_chunking_router)
# Search in collection
app.include_router(searching_router)

if __name__ == "__main__":
    uvicorn.run("server:app",host="127.0.0.1",port=8080,reload=False)

