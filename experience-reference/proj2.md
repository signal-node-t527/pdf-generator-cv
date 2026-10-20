# Suggestion Engine

The Suggestion Engine is an AI-powered platform designed to provide intelligent suggestions for chat-based interactions. It utilizes Retrieval-Augmented Generation (RAG) and semantic search to guide users based on historically successful conversation patterns.

## Project Architecture

The project is composed of several microservices orchestrated via Docker:

### 1. **se-gui** (Frontend)
- **Technology:** Angular, TypeScript, SCSS.
- **Role:** The user interface for the platform. It allows users to manage groups, view chat sessions, and interact with the suggestion engine.

### 2. **se-api** (Backend API)
- **Technology:** ASP.NET Core (.NET 9), C#.
- **Role:** The central management API and secure gateway.
- **Key Responsibilities:**
    - Authentication and authorization (JWT).
    - Management of Users, Groups, Categories, and Sessions.
    - Proxying and securing requests to the `se-core` microservice.
    - Business logic for group configuration and metric injection.

### 3. **se-core** (AI Logic Service)
- **Technology:** FastAPI, Python, Google GenAI (Gemini).
- **Role:** The core AI processing engine.
- **Key Responsibilities:**
    - **Fragmentation:** Converts linear chat histories into structured interaction units (Context -> Input -> Response).
    - **Vectorization:** Generates semantic embeddings for chat fragments using Google GenAI.
    - **Success Evaluation:** Automatically rates the quality of interactions based on configurable metrics using LLMs.
    - **Consultation (RAG):** Performs semantic search in the vector database to find successful past interactions and generate suggestions.
    - **Knowledge Base:** Manages the storage and retrieval of "reports" (evaluated interactions).

### 4. **se-db** (Database)
- **Technology:** PostgreSQL 16 with `pgvector` extension.
- **Role:** Unified storage for application data and the vector-indexed knowledge base.

---

## Key Workflows

### **Contribute (Report)**
1. A chat interaction is sent to the system.
2. `se-core` fragments the conversation and evaluates its "success weight" (0.0 to 1.0) based on group-defined metrics.
3. If successful, the interaction is vectorized and saved to the database.
4. This builds a shared knowledge base of "what works" for a specific group or goal.

### **Consult (Suggest)**
1. The user requests a suggestion for the current conversation context.
2. `se-core` vectorizes the recent context and searches the database for semantically similar, high-success reports.
3. It uses the most relevant examples as context for an LLM to generate a tailored suggestion.
4. The system can also consider "what NOT to do" by looking at low-success reports.

---

## Technology Stack

- **AI/LLM:** Google Gemini 2.0 (Flash & Embedding).
- **Backend:** C# (.NET 9), Python (FastAPI).
- **Frontend:** Angular (v19+).
- **Database:** PostgreSQL + pgvector.
- **DevOps:** Docker, Docker Compose.

---

## Deployment

The project is designed to run in a containerized environment. Use Docker Compose to spin up the entire stack:

```bash
docker-compose up --build
```

Access the application at `http://localhost`. The API is exposed at `http://localhost:5000`.
