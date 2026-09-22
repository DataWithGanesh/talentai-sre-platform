from fastapi import FastAPI

from app.api.routes import router as common_router
from app.api.auth_routes import router as auth_router

app = FastAPI(
    title="Auth Service",
    version="1.0.0"
)

app.include_router(common_router)
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def root():
    return {
        "service": "Auth Service",
        "status": "running"
    }