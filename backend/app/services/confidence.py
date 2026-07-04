"""
Estimate confidence score.
"""


def confidence_score(reasons):

    score = len(reasons) * 25

    if score > 100:
        score = 100

    return score