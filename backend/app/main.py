from fastapi import FastAPI

from app.db.base import Base
from app.db.postgres import engine

from app.api.health import router as health_router
from app.api.alerts import router as alert_router
from app.api.graph import router as graph_router
from app.api.investigate import router as investigate_router
from app.api.rag import router as rag_router
from app.api.history import router as history_router
from app.api.investigation import router as explain_router
from app.api.threat import router as threat_router
from app.api.audit import router as audit_router
from app.api.dashboard import router as dashboard_router
from app.api.auth import router as auth_router

from app.middleware.logging import LoggingMiddleware
from app.config.constants import APP_NAME, VERSION

from app.api.case_notes import router as case_notes_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    version=VERSION
)

app.add_middleware(LoggingMiddleware)

app.include_router(health_router)
app.include_router(alert_router)
app.include_router(graph_router)
app.include_router(investigate_router)
app.include_router(rag_router)
app.include_router(history_router)
app.include_router(explain_router)
app.include_router(threat_router)
app.include_router(audit_router)
app.include_router(dashboard_router)
app.include_router(auth_router)
app.include_router(case_notes_router)

@app.get("/")
def root():
    return {"message": "AI SOC Copilot Running 🚀"}