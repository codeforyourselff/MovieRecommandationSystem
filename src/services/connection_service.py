import os
from qdrant_client import QdrantClient
from threading import Lock
from dotenv import load_dotenv

load_dotenv()

class connection_to_cluster:
    _instance = None
    _lock = Lock()

    def __init__():
        pass

    def __new__(cls):
        try:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = QdrantClient(url=os.getenv("QDRANT_URL"),api_key=os.getenv("QDRANT_API"),cloud_inference=True)
            return cls._instance
        except Exception as e:
            print(e)