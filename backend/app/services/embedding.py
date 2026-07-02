import hashlib


def create_embedding(text: str):

    digest = hashlib.sha256(
        text.encode()
    ).digest()

    vector = []

    for byte in digest:

        vector.append(byte / 255)

    return vector