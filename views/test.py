import requests


API_URL = 'http://127.0.0.1:8000/'

def get_connection_by_id(id_connection):
    connection_data = []
    
    # Primeira requisição para obter os dados da conexão específica
    response = requests.get(API_URL + f'/connections/{id_connection}')
    
    if response.status_code == 200:
        connection_data.append(response.json())
    
    return connection_data


dados = get_connection_by_id(4)
dados