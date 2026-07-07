"""
Tool Registry

Single place where every external tool
is registered.

Later this becomes MCP Registry.
"""

from app.tools.virustotal import lookup_ioc
from app.tools.mitre import lookup_attack


TOOLS = {

    "virustotal": lookup_ioc,

    "mitre": lookup_attack

}


def use_tool(tool_name: str, value: str):

    tool = TOOLS.get(tool_name)

    if tool is None:

        return {

            "error": "Tool not found"

        }

    return tool(value)