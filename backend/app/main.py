from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.alerts import router as alert_router

from app.db.base import Base
from app.db.postgres import engine

from app.api.graph import router as graph_router

from app.api.investigate import router as investigate_router

from app.api.rag import router as rag_router

from app.api.investigate import router as investigate_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI SOC Copilot",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(alert_router)
app.include_router(graph_router)
app.include_router(investigate_router)
app.include_router(rag_router)
app.include_router(investigate_router)

@app.get("/")
def root():
    return {"message": "AI SOC Copilot Running 🚀"}