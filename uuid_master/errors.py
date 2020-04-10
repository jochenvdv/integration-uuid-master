import json

from flask import make_response


def make_error_response(error_msg, status_code):
    return make_response(json.dumps({'error': error_msg}), status_code)


def return_404():
    return make_error_response('Not found', 404)
