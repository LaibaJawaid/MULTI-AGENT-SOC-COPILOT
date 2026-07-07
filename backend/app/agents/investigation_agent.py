from app.services.investigator import investigate_alert
from app.tools.registry import use_tool


class InvestigationAgent:

    def run(self, alert):

        result = investigate_alert(alert)

        return {

            "alert_id": alert.id,

            "analysis": result

        }


agent = InvestigationAgent()