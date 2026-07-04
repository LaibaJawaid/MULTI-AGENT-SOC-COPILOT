"""
Recommendation Agent

Uses recommendation service.
"""

from app.services.recommendation import generate_recommendations


def recommend(alert: dict):

    recommendations = generate_recommendations(alert)

    return {

        "recommendations": recommendations

    }