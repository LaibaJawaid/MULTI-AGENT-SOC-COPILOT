"""
MCP Registry

Stores every available tool.

Supervisor Agent asks this registry
which tools exist.
"""

from app.mcp.tools import (

    firewall_block,

    isolate_host,

    create_ticket

)

TOOLS = {

    "firewall": firewall_block,

    "endpoint": isolate_host,

    "ticket": create_ticket

}