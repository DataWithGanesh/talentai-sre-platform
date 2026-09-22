from fastapi import FastAPI

app = FastAPI(
    title="Resume Service",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "Resume Service",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }