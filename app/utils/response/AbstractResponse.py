from flask import jsonify

from app.utils.response import Response


def do():
    pass


def execute():
    try:
        return jsonify(Response.ok(do()))
    except Exception as e:
        return Response.fail(e)
