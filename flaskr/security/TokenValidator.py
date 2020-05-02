import functools

import jwt
import yaml
from flask import jsonify

app_config = yaml.load(open('app_config.yml'))


def token_validator(request):
    def token_required(f):
        @functools.wraps(f)
        def decorate(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing.'}), 401
            try:
                data = jwt.decode(token, app_config['config']['key'])
            except:
                return jsonify({'message': 'Token is invalid.'}), 401
            return f(*args, **kwargs)

        return decorate

    return token_required
