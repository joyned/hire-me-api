from flask import Flask, jsonify, request, app
from flask import Blueprint

job_service = Blueprint('job_service', __name__)


@job_service.route('/api/job', methods=['POST'])
def save_new_job():
    return jsonify("working!")
