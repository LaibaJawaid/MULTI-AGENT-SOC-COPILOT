from pydantic import BaseModel

class InvestigationRequest(BaseModel):
    title: str
    description: str
    severity: str


class InvestigationResponse(BaseModel):
    classification: str
    severity: str
    summary: str
    playbook: str
    graph_entities: list


class InvestigationResult(BaseModel):

    severity: str

    summary: str

    confidence: int

    reasons: list[str]