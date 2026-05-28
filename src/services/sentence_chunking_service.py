import os
from llama_index.core.node_parser import SentenceSplitter

class sentence_chunking_service:
    def __init__(self):
        self.max_tokens = int(os.getenv("MAX_TOKENS",100))
        self.overlap_tokens = int(os.getenv("OVERLAP_TOKENS",10))

    async def sentence_chunking(self,text):
        dataset = []
        splitter = SentenceSplitter(chunk_size=self.max_tokens, chunk_overlap=self.overlap_tokens)
        for i in text:
            dataset.append(splitter.split_text(i["description"]))
        return dataset 
        