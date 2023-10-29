from flask import Blueprint, render_template, request, redirect, url_for, jsonify, abort
import requests
from decouple import config
 
script_bp = Blueprint('script', __name__, template_folder="./templates", static_folder="static")

API_URL = config('API_URL')

@script_bp.route('/view_script/<int:id_project>', methods=['GET', 'POST'])
def view_script(id_project):
    if request.method == 'GET':
        try:
            response = requests.get(API_URL + f'/GetqueriesIdprojects/{id_project}') 
            if response.status_code == 200:
                query_data = response.json()
            else:
                query_data = []
            return render_template('scripts/views_script.html', query_data=query_data)
        except Exception as e:
            return render_template('error/error.html', error = str(e))
    else:
        abort(405, "Método não suportado. Apenas o método GET é permitido nesta rota.")
 
@script_bp.route('/create_script/', methods=['POST'])
def create_script():
    try:
        if request.method == 'POST':
            id_project = request.form.get('id_project')
            origin_query = request.form.get('origin_query')
            query_destination = request.form.get('query_destination')
            id_type_query = request.form.get('id_type_query')
            nr_execution_order = request.form.get('nr_execution_order')

            data = {
                'id_project': id_project,
                'origin_query': origin_query,
                'query_destination': query_destination,
                'id_type_query': id_type_query,
                'nr_execution_order': nr_execution_order
            }

            response = requests.post(API_URL + '/CreateQueries', json=data) 

            if response.status_code == 200:
                return redirect(url_for('script.view_script', id_project=id_project))
    except Exception as e:
        return render_template('error/error.html', error=str(e))



@script_bp.route('/update_query/<int:id_query>', methods=['POST', 'GET'])
def update_query(id_query):
    try:
        if request.method == 'GET':
            response = requests.get(f'{API_URL}/GetQueriesId/{id_query}')
            if response.status_code == 200:
                data_edit_query = response.json()
            else:
                data_edit_query = []
            return render_template('scripts/edit_script.html', data_edit_query=data_edit_query)
            
        if request.method ==  'POST':
            id_project = request.form.get('id_project')
            origin_query = request.form.get('origin_query')
            query_destination = request.form.get('query_destination')
            id_type_query = request.form.get('id_type_query')
            nr_execution_order = request.form.get('nr_execution_order')
            
            data = {
                'id_project': id_project,
                'origin_query': origin_query,
                'query_destination': query_destination,
                'id_type_query': id_type_query,
                'nr_execution_order': nr_execution_order
            }

            response = requests.put(API_URL + f'/UpdateQueries/{id_query}', json=data)
            if response.status_code == 200:
                return redirect(url_for('script.view_script', id_project=id_project))
            else:
                return "Erro ao atualizar a consulta via API"
        else:
           return redirect(url_for('script.view_script', id_project=id_project))
    except Exception as e:
        return render_template('error/error.html', error=str(e))

@script_bp.route('delete_query/<int:id_query>/<int:id_project>', methods=['GET'])
def delete_query(id_query, id_project):
    try:
        if request.method == 'GET':
            response = requests.delete( API_URL + f'/DeleteQueries/{id_query}')
            if response.status_code == 200:
                return redirect(url_for('script.view_script', id_project=id_project))
        else:
            pass
    except Exception as e:
        return render_template('error/error.html', error=str(e))

       


