import os
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

class fixed_chunking_service:

    def __init__(self):
        self.max_tokens = int(os.getenv("MAX_TOKENS", 40))

    async def fixed_size_chunks(self,item):
        tokens = tokenizer.encode(item["description"], add_special_tokens=False)

        text_chunks = [
                tokenizer.decode(tokens[i:i+self.max_tokens], skip_special_tokens=True)
                for i in range(0, len(tokens), self.max_tokens)
        ]

        flat_chunks = []
        for i,text in enumerate(text_chunks):
            flat_chunks.append({"movie_name":item["name"],"author":item["author"],"year":item["year"],"chunk":text})
        return flat_chunks