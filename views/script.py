from flask import Blueprint, render_template, request, redirect, url_for, jsonify, abort
from datetime import datetime
import requests
from decouple import config

script_bp = Blueprint('script', __name__, template_folder="./templates", static_folder="static")

API_URL = config('API_URL')

@script_bp.route('/view_script/<int:id_project>', methods=['GET', 'POST'])
def view_script(id_project):
    if request.method == 'GET':
        response = requests.get(API_URL + f'/GetqueriesIdprojects/{id_project}') 
        if response.status_code == 200:
            query_data = response.json()

            return render_template('scripts/views_script.html', query_data=query_data)
        else:
            return "Erro ao obter os detalhes do projeto"