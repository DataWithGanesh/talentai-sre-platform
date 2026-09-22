from fastapi import FastAPI

app = FastAPI(
    title="AI Screening Service",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "AI Screening Service",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }