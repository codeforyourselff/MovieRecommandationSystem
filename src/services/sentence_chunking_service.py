import os
from llama_index.core.node_parser import SentenceSplitter, SemanticSplitterNodeParser

class sentence_chunking_service:
    MAX_TOKENS = os.getenv("MAX_TOKENS",40)
    def __init__(self):
        pass

    async def sentence_chunking(self,text):
        """Sentence-aware chunking: respects sentence boundaries"""
        splitter = SentenceSplitter(chunk_size=self.MAX_TOKENS, chunk_overlap=10)
        return splitter.split_text(text)
        