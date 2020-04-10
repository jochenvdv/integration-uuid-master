import random
import string
import uuid

_API_KEY_LENGTH = 64


def create_api_key():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(_API_KEY_LENGTH))


def create_uuid():
    return str(uuid.uuid4())