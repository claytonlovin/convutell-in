from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import requests
from decouple import config

logs_bp = Blueprint('logs', __name__, template_folder="./templates", static_folder="static")


# DEFINIR URL
API_URL = config('API_URL')

@logs_bp.route('/logs/<int:id_project>')
def get_log(id_project):
	response = requests.get(API_URL + f'/GetlogId/{id_project}')
	if response.status_code == 200:
		log = response.json()
	else:
		log = []

	return render_template('logs/logs.html', log = log)

@logs_bp.route('/logs/logsall', methods=['GET'])
def get_all_logs():
    response = requests.get(API_URL + '/GetAlllog')

    if response.status_code == 200:
        log = response.json()
    else:
        log = []

    return render_template('logs/logs.html', log=log)
