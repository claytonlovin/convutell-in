from flask import Blueprint, render_template, request, redirect, url_for, jsonify, abort
from datetime import datetime
import requests
from decouple import config

connection_bp = Blueprint('conection', __name__, template_folder="./templates", static_folder="static")

API_URL = config('API_URL')



@connection_bp.route('/connection/')
def get_connection():
    try:
        response = requests.get(API_URL + f'/connections/')
        if response.status_code == 200:
            conection = response.json()
        else:
            conection = []
        return render_template('connections/connection.html', conection=conection)
    except Exception as e:
            return render_template('error/error.html', error = str(e))
    

@connection_bp.route('/view_connection/<int:id_connection>')
def get_connection_by_id(id_connection):
    try:
        response = requests.get(API_URL + f'/connections/{id_connection}')
        if response.status_code == 200:
            connection = response.json()
        else:
            connection = []
        return render_template('connections/view_connection.html', connection=connection)
    except Exception as e:
            return render_template('error/error.html', error = str(e))

@connection_bp.route('/create_connection/', methods=['POST'])
def create_connection():
    if request.method == 'POST':
        try:
            ds_name_connection = request.form.get('ds_name_connection')
            ds_user = request.form.get('ds_user')
            ds_connection = request.form.get('ds_connection')
            ds_password = request.form.get('ds_password')
            ds_port = request.form.get('ds_port')
            ds_database = request.form.get('ds_database')
            ds_connector = request.form.get('ds_connector')

            data = {
                'ds_name_connection' : ds_name_connection,
                'ds_user': ds_user,
                'ds_connection': ds_connection,
                'ds_password': ds_password,
                'ds_port': ds_port,
                'ds_database': ds_database,
                'ds_connector': ds_connector
            }
            response = requests.post( API_URL + '/connections', json=data) 

            if response.status_code == 200:
                return redirect(url_for('conection.get_connection')) 
        except Exception as e:
            return render_template('error/error.html', error = str(e))
