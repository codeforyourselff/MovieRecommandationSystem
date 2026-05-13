from sentence_transformers import SentenceTransformer

class embedding_model:
    def __init__(self):
        pass

    def get_embedding(self):
        return SentenceTransformer("all-miniLM-L6-v2")