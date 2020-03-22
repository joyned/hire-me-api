import pyrebase
from flask import jsonify

config = {
    "apiKey": "AIzaSyAsBtBjcuEu4ZEF0irkefd9v62iy-XCR54",
    "authDomain": "surfshop-3c920.firebaseapp.com",
    "databaseURL": "https://surfshop-3c920.firebaseio.com",
    "projectId": "surfshop-3c920",
    "storageBucket": "surfshop-3c920.appspot.com",
    "messagingSenderId": "139153291264",
    "appId": "1:139153291264:web:23732b8af4ea935d98c0e5",
    "measurementId": "G-GB8K4SS15V"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


def auth_user(email, pwd):
    return auth.sign_in_with_email_and_password(email, pwd)
