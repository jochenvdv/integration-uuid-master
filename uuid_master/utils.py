import random
import string

_API_KEY_LENGTH = 64


def create_api_key():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(_API_KEY_LENGTH))


def get_app_from_auth(request):
    pass