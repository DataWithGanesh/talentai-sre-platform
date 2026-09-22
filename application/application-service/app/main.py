from fastapi import FastAPI

app = FastAPI(
    title="Application Service",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "Application Service",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }