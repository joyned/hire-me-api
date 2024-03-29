from app.model.response.ResponseModel import ResponseModel
import logging


def ok(data):
    return response(data, True)


def fail(data):
    return response(str(data), False)


def response(data, ok):
    res = ResponseModel()
    res.ok = ok
    res.payload = data

    return res.serialize()


def execute(func, *args, error_status_code):
    try:
        return ok(func(*args))
    except Exception as e:
        logging.error(e)
        return fail(e), error_status_code


def ok_message(message):
    return {'message': message}


def fail_message(message):
    return {'fail': message}
