from flaskr.auth import auth
from flaskr.service.JobService import job_service
from flaskr.service.UserService import user_service

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__, template_folder="html")

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(job_service)
app.register_blueprint(user_service)

user = "admin@admin.com"
pwd = "123456"


@app.route('/api/test', methods=['GET'])
def test():
    return jsonify(auth.auth_user(user, pwd))


if __name__ == '__main__':
    app.run(debug=True)
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
