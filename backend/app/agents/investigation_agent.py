from app.services.investigator import investigate_alert


class InvestigationAgent:

    def run(self, alert):

        result = investigate_alert(alert)

        return {

            "alert_id": alert.id,

            "analysis": result

        }


agent = InvestigationAgent()