import os
from llama_index.core import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SemanticSplitterNodeParser

class semantic_chunking_service:
    
    def __init__(self):
        self._buffer_size = os.getenv("BUFFER_SIZE")
        self._breakpoint_percentile_threshold = os.getenv("BREAKPOINT_PERCENTILE_THRESHOLD")
        self._embed_model = os.getenv("EMBED_MODEL")
        self.semantic_splitter = SemanticSplitterNodeParser(
            buffer_size=int(self._buffer_size),
            breakpoint_percentile_threshold=int(self._breakpoint_percentile_threshold),
            embed_model=HuggingFaceEmbedding(model_name=self._embed_model)
        )

    async def semantic_chunking(self,text):
        documents = []
        for item in text:
            description = item.get("description","")
            if not description:
                continue

            document = Document(text=description,metadata={
                "movie_name": item.get("name"),
                "author": item.get("author"),
                "year": item.get("year")
            })
            documents.append(document)
        

        return await self.semantic_splitter.get_nodes_from_documents(documents)


    