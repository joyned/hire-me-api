import random
import os

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from Book import Book
from Movie import Movie

app = Flask(__name__, template_folder="html")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# movie = Movie()
# movie.id = i
# movie.name = 'Movie ' + str(i)
# movie.description = 'This is a description.'
# data.append(movie.serialize())

def create_all(size):
    data = []
    for i in range(size):
        book = Book()
        book.id = i
        book.book_code = random.randint(1, 1000)
        book.read_status = 'Complete'
        book.name = 'Book ' + str(i)
        book.price = random.randint(1, 1000)
        data.append(book.serialize())
    return data


def create_any(size):
    data = []
    n = int(size / 2)
    for i in range(n):
        book = Book()
        book.id = i
        book.book_code = random.randint(1, 1000)
        book.read_status = 'Complete'
        book.name = 'Book ' + str(i)
        book.price = random.randint(1, 1000)
        data.append(book.serialize())
    for i in range(n):
        movie = Movie()
        movie.id = i
        movie.name = 'Movie ' + str(i)
        movie.description = 'This is a description.'
        data.append(movie.serialize())
    return data


@app.route('/api/any/<size>', methods=['POST'])
def get_any(size):
    data = create_any(int(size))
    return jsonify(data)


@app.route('/api/array/<size>', methods=['POST'])
def get_book(size):
    data = create_all(int(size))
    return jsonify(data)


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify("{success: {} }".format(validate_login(data.get('user'), data.get('password'))))


def validate_login(user, pwd):
    if user == 'admin' and pwd == 'admin':
        return True
    else:
        return False


@app.route('/api/test', methods=['GET'])
def test():
    return jsonify('working!')


if __name__ == '__main__':
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
