from abc import abstractmethod

from flask import jsonify

from flaskr.response import Response


def do():
    pass


def execute():
    try:
        return jsonify(Response.ok(do()))
    except Exception as e:
        return Response.error(e)
