"""
Stores completed investigations.

Currently uses in-memory list.

Later:
Replace with PostgreSQL.
"""

# Temporary storage
# Will later move to PostgreSQL
history = []


def save_investigation(result: dict):
    """
    Save investigation.
    """
    history.append(result)


def get_history():
    """
    Return all investigations.
    """
    return history