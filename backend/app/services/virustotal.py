"""
VirusTotal Service

Later:

Will call

https://www.virustotal.com/api/

Currently returns fake data.
"""


def lookup(hash_value):

    return {

        "hash": hash_value,

        "malicious": True,

        "detections": 48

    }