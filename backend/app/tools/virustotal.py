"""
VirusTotal Tool

Currently mocked.

Later:
Replace this with actual VirusTotal API.
"""


def lookup_ioc(ioc: str):

    # TODO:
    # Real VirusTotal API call

    return {

        "ioc": ioc,

        "malicious": True,

        "detections": 41,

        "source": "VirusTotal"

    }