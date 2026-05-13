import os
from llama_index.core import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SemanticSplitterNodeParser

class semantic_chunking_service:
    _buffer_size = os.getenv("BUFFER_SIZE")
    _breakpoint_percentile_threshold = os.getenv("BREAKPOINT_PERCENTILE_THRESHOLD")
    _embed_model = os.getenv("EMBED_MODEL")
    
    def __init__(self):
        pass

    async def semantic_chunking(self,text):
        semantic_splitter = SemanticSplitterNodeParser(
            buffer_size=int(self._buffer_size),
            breakpoint_percentile_threshold=int(self._breakpoint_percentile_threshold),
            embed_model=HuggingFaceEmbedding(model_name=self._embed_model)
        )
        nodes = semantic_splitter.get_nodes_from_documents([Document(text=text)])
        return [node.text for node in nodes]