import functools

import jwt
import yaml
from flask import jsonify

from app.utils.resource import ResourceUtil

app_config = ResourceUtil.get_resource_file('app_config.yml')


def token_validator(request):
    def token_required(f):
        @functools.wraps(f)
        def decorate(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing.'}), 401
            try:
                jwt.decode(token, app_config['config']['key'])
            except:
                return jsonify({'message': 'Token is invalid.'}), 401
            return f(*args, **kwargs)

        return decorate

    return token_required


def token_decode(request):
    token = request.headers.get('Authorization')
    return jwt.decode(token, app_config['config']['key'])
