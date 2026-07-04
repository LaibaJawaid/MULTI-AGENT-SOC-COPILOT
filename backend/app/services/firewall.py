"""
Firewall Service

Currently Dummy.

Later

↓

Cisco

↓

Fortinet

↓

Palo Alto

↓

Checkpoint
"""


def block(ip):

    return {

        "blocked": True,

        "ip": ip

    }