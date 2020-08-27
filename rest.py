import os

from flaskr.service.JobService import job_service
from flaskr.service.UserService import user_service
from flaskr.service.PageService import page_service
from flaskr.service.PersonService import person_service
from flaskr.service.LoginService import login_service
from flaskr.service.RegisterService import register_service

from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder="html")

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(job_service)
app.register_blueprint(user_service)
app.register_blueprint(page_service)
app.register_blueprint(person_service)
app.register_blueprint(login_service)
app.register_blueprint(register_service)

if __name__ == '__main__':
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)