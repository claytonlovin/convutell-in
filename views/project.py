from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import requests
from decouple import config

projects_bp = Blueprint('projects', __name__, template_folder="./templates", static_folder="static")


# DEFINIR URL
API_URL = config('API_URL')


def get_connections_list():
    connections_list = []
    response = requests.get(API_URL + '/connections')
    if response.status_code == 200:
        connections_list = response.json()
    return connections_list

def get_connection_by_id(id_connection):
    connection_data = []
    
    response1 = requests.get(API_URL + f'/connections/{id_connection}')
    
    if response1.status_code == 200:
        try:
            data1 = response1.json()
            connection_data.append(data1)
        except ValueError:
            print("Erro: A resposta da primeira requisição não é um JSON válido.")
    
    response2 = requests.get(API_URL + '/connections')
    
    if response2.status_code == 200:
        try:
            data2 = response2.json()
            connection_data.extend(data2)
        except ValueError:
            print("Erro: A resposta da segunda requisição não é um JSON válido.")
    
    return connection_data

@projects_bp.route('/')
def show_projects():
    end = API_URL + '/GetAllProjects'  
    response = requests.get(end)

    if response.status_code == 200:
        projects = response.json()
    else:
        projects = []

    for project in projects:

        project['dt_last_run'] = datetime.fromisoformat(project['dt_last_run'])
        project['dt_last_run'] = project['dt_last_run'].strftime('%d/%m/%Y %H:%M:%S')

    return render_template('projects/list_projects.html', projects=projects)


@projects_bp.route('/create_project', methods=['GET', 'POST'])
def create_project():
    connections_list = get_connections_list()

    if request.method == 'GET':
        return render_template('projects/create_project.html', connections_list=connections_list)
    
    if request.method == 'POST':
        name_project = request.form.get('name_project')
        fl_active = request.form.get('fl_active')
        connection_origin1 = request.form.get('connection_origin1')
        connection_origin2 = request.form.get('connection_origin2')
        current_datetime = datetime.now()
        dt_last_run = current_datetime.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        project = {
            'name_project': name_project,
            'dt_last_run': dt_last_run,
            'fl_active': fl_active,
            'connection_origin1': connection_origin1,
            'connection_origin2': connection_origin2,
        }

        response = requests.post( API_URL + '/CreateProjects', json=project) 

        if response.status_code == 200:
            return redirect(url_for('projects.show_projects')) 
        else:

            return "Erro ao criar o projeto"

    return redirect(url_for('projects.show_projects'))
    
 

@projects_bp.route('/view_project/<project_id>', methods=['GET', 'POST'])
def view_project(project_id):
    if request.method == 'GET':
        response = requests.get(API_URL + f'/GetProjectsId/{project_id}') 
        if response.status_code == 200:
            project_data = response.json()
            
            connection_origin1 = get_connection_by_id(project_data['connection_origin1'])
            connection_origin2 = get_connection_by_id(project_data['connection_origin2'])
            
            return render_template('projects/view_project.html', project=project_data, 
                                   connection_origin1=connection_origin1, connection_origin2=connection_origin2)
        else:
            return "Erro ao obter os detalhes do projeto"

@projects_bp.route('/edit_project/<int:id_project>', methods=['POST'])  
def edit_project(id_project):
    if request.method == 'POST':
        name_project = request.form.get('name_project')
        fl_active = request.form.get('fl_active')
        connection_origin1 = request.form.get('connection_origin1')
        connection_origin2 = request.form.get('connection_origin2')
        project = {
            'name_project': name_project,
            'fl_active': fl_active,
            'connection_origin1': connection_origin1,
            'connection_origin2': connection_origin2,
        }
        response = requests.put(API_URL + f'/GetProjectsId/{id_project}', json=project)

        if response.status_code == 200:
            return redirect(url_for('projects.show_projects'))
        else:
            return "Erro ao atualizar o projeto"

    return redirect(url_for('projects.show_projects'))


@projects_bp.route('/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    if request.method == 'POST':
        try:
            api_url =  API_URL + '/DeleteProjects/{project_id}'
            response = requests.delete(api_url)

            if response.status_code == 200:
                return jsonify({"message": "Projeto excluído com sucesso"})
            else:
                return jsonify({"error": "Erro ao excluir o projeto"})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        pass
    