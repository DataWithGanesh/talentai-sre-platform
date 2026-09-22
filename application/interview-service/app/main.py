from fastapi import FastAPI

app = FastAPI(
    title="Interview Service",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "Interview Service",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }