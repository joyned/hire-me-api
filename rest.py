import os

import yaml
from flask import Flask
from flask_cors import CORS

from app.rest.job.JobRest import job_rest
from app.rest.login.LoginRest import login_rest
from app.rest.page.PageRest import page_rest
from app.rest.person.PersonRest import person_rest
from app.rest.register.RegisterRest import register_rest
from app.rest.user.UserRest import user_rest

app = Flask(__name__, template_folder="html")

environment = yaml.load(open('resource/environment.yml'))

production = environment['environment']['production']

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(job_rest)
app.register_blueprint(user_rest)
app.register_blueprint(page_rest)
app.register_blueprint(person_rest)
app.register_blueprint(login_rest)
app.register_blueprint(register_rest)

if __name__ == '__main__':
    if production:
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(debug=True)
