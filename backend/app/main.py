from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="AI SOC Copilot",
    version="1.0.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "AI SOC Copilot Running 🚀"
    }