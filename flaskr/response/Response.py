from flask import jsonify

from flaskr.model.ResponseModel import ResponseModel


def ok(data):
    return response(data, True)


def error(data):
    return response(str(data), False)


def response(data, ok):
    res = ResponseModel()
    res.ok = ok
    res.payload = data

    return res.serialize()
