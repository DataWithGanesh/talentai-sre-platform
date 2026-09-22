from fastapi import FastAPI

app = FastAPI(
    title="Job Service",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "Job Service",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }