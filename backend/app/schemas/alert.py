from pydantic import BaseModel


class AlertCreate(BaseModel):

    title: str

    description: str


class AlertResponse(BaseModel):

    id: int

    title: str

    description: str

    severity: str

    category: str

    summary: str

    recommendation: str

    status: str

    class Config:

        from_attributes = True