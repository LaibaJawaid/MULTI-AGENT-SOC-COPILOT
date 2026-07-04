"""
MCP Tools

Every function in this file represents
one tool that the AI Agent can use.

Later:

- VirusTotal
- Firewall
- Splunk
- CrowdStrike
- Jira

will all be here.
"""


def firewall_block(ip: str):
    """
    Simulates blocking an IP address.

    Later this will call
    Firewall REST API.
    """

    return {

        "tool": "Firewall",

        "action": "Block IP",

        "ip": ip,

        "status": "SUCCESS"

    }


def isolate_host(hostname: str):
    """
    Simulates host isolation.

    Later:
        CrowdStrike
        Defender
    """

    return {

        "tool": "Endpoint",

        "action": "Isolate Host",

        "host": hostname,

        "status": "SUCCESS"

    }


def create_ticket(title: str):
    """
    Creates SOC ticket.

    Later:
        Jira API
        ServiceNow API
    """

    return {

        "tool": "Jira",

        "ticket": title,

        "status": "CREATED"

    }