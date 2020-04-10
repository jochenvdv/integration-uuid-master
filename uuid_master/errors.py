import json

from flask import make_response


def make_error_response(error_msg, status_code):
    return make_response(
        json.dumps({'error': error_msg}),
        status_code,
        {'Content-Type': 'application/json'}
    )


def create_400():
    return make_error_response('Bad request', 400)


def create_401():
    return make_error_response('Unauthorized', 401)


def create_404():
    return make_error_response('Not found', 404)
