from sqlalchemy.orm import Session

from app.services.classifier import classify_alert

from app.services.severity import calculate_severity

from app.services.deduplication import is_duplicate

from app.services.gpt_service import generate_summary

from app.services.remediation import recommend_action

from app.services.GraphandQuery import get_related


def analyze_alert(db: Session, alert):

    duplicate = is_duplicate(
        db,
        alert.title
    )

    category = classify_alert(
        alert.title,
        alert.description
    )

    severity = calculate_severity(
        alert.description
    )

    summary = generate_summary(
        alert.title,
        alert.description
    )

    actions = recommend_action(
        category
    )

    related = get_related(category)

    return {

        "duplicate": duplicate,

        "category": category,

        "severity": severity,

        "summary": summary,

        "actions": actions,

        "related": related

    }

