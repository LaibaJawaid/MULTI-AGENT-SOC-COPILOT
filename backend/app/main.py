from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.alerts import router as alert_router

from app.db.base import Base
from app.db.postgres import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI SOC Copilot",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(alert_router)


@app.get("/")
def root():
    return {"message": "AI SOC Copilot Running 🚀"}