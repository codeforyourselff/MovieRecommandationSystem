# Movie Recommendation System (MRC) 🎬

A powerful, AI-driven Movie Recommendation System backend built with **FastAPI** and **Qdrant**. This API processes movie descriptions, performs intelligent text chunking, generates embeddings, and manages vector databases to power highly accurate, semantic movie recommendations.

## 🚀 Features

- **Vector Database Integration:** Full CRUD support for managing [Qdrant](https://qdrant.tech/) collections.
- **Advanced Text Chunking Strategies:** Optimized embedding generation using multiple text chunking techniques:
  - **Fixed-Size Chunking:** Breaks text down into consistent token sizes.
  - **Sentence Chunking:** Intelligently splits descriptions by sentence boundaries.
  - **Semantic Chunking:** Context-aware splitting to retain meaning across chunks using `LlamaIndex`.
- **High-Performance Embeddings:** Powered by `sentence-transformers` (using models like `all-MiniLM-L6-v2`) to convert text into high-dimensional vector representations.
- **FastAPI Backend:** Fully asynchronous, blazing-fast API with automatic Swagger/OpenAPI documentation.

## 🛠️ Tech Stack

- **Framework:** FastAPI, Uvicorn
- **Vector Search Engine:** Qdrant (`qdrant_client`)
- **Machine Learning / NLP:** `sentence_transformers`, `transformers`, `llama_index`
- **Data Validation:** Pydantic

## 📂 Project Structure

```text
src/
├── controllers/      # FastAPI Routers (Collections, Chunking strategies)
├── models/           # Pydantic schemas and Data Models
└── services/         # Core business logic (Qdrant connection, embedding logic, etc.)
```

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/codeforyourselff/MovieRecommandationSystem.git
   cd MovieRecommandationSystem
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Make sure you have your `.env` configured (e.g., Qdrant cluster URLs, API keys, Model max tokens, etc.).

5. **Run the server**
   ```bash
   python -m uvicorn server:app --reload --port 8080
   ```

## 📚 API Documentation

Once the server is running, navigate to the auto-generated documentation to explore and test the endpoints:
- **Swagger UI:** [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
- **ReDoc:** [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)

### Core Endpoints Overview:
- `GET /` - Root health check
- **Collections:** 
  - `POST /v1/collection/create_collection`
  - `GET /v1/collection/collection_info/{collection_name}`
  - `DELETE /v1/collection/delete_collection/{collection_name}`
- **Chunking & Uploading:**
  - `POST /v1/chunking/fixed_size_chunks`
  - `POST /v1/chunking/sentence_chunks`
  - `POST /v1/chunking/semantic_chunks`
