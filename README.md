# Course Chatbot

Search-based chatbot (BM25 + field lookup) for course details. No LLM needed.

## Run
    python -m venv .venv
    .venv\Scripts\activate        # Windows
    source .venv/bin/activate      # macOS / Linux
    pip install -r requirements.txt
    uvicorn app.main:app --reload

Then open http://127.0.0.1:8000/health
