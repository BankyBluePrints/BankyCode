# Streamlit knowledge-base prototype

A static UI prototype that demonstrates suggested questions, answers, and metadata using
synthetic data. It does not call Confluence, an LLM, or any external API.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r examples/streamlit-knowledge-base/requirements.txt
streamlit run examples/streamlit-knowledge-base/app.py
```

The sample intentionally avoids unsafe HTML rendering and artificial network/loading
behavior.
