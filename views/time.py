from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import requests
from decouple import config

times_bp = Blueprint('times', __name__, template_folder="./templates", static_folder="static")

API_URL = config('API_URL')

@times_bp.route('/times/<int:id_project>')
def get_times(id_project):
    response = requests.get(API_URL + f'/GetTimesId/{id_project}')
    if response.status_code == 200:
        times = response.json()
    else:
        times = []

    return render_template('time/times.html', times=times)


@times_bp.route('/delete_time/<int:id_time>', methods=['POST'])
def delete_time(id_time):
    if request.method == 'POST':
        try:
            api_url = f"{API_URL}/DeleteTimes/{id_time}"
            response = requests.delete(api_url)

            if response.status_code == 200:
                return redirect(url_for('projects.show_projects'))
            else:
                return jsonify({"error": "Erro ao excluir o Time"})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        pass

@times_bp.route('/edit_time/<int:id_time>', methods=['POST'])
def edit_time(id_time):
    if request.method == 'POST':
        try:
            id_time  = request.form.get('id_time')
            id_project  = request.form.get('id_project')
            time  = request.form.get('time')
            
            time_data = {
                'id_time': id_time,
                'id_project': id_project,
                'time': time
            }
            api_url = f"{API_URL}/UpdateTimes/{id_time}"
            response = requests.put(api_url, json=time_data)

            if response.status_code == 200:
                return redirect(url_for('projects.show_projects'))
            else:
                return jsonify({"error": "Erro ao editar o horário"})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        pass
