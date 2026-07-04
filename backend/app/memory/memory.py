"""
LangGraph Memory

Stores previous investigations.
"""

from langgraph.checkpoint.memory import MemorySaver

# In-memory checkpoint (development)
# LangGraph memory object
# Used for checkpointing graph execution
memory = MemorySaver()