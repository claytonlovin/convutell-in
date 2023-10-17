from flask import Flask
from views.project import projects_bp
from views.logs import logs_bp
from views.time import times_bp
#from connections import connections_bp
from decouple import config

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(projects_bp, url_prefix='/projects')
app.register_blueprint(logs_bp, url_prefix='/logs')
app.register_blueprint(times_bp, url_prefix='/times')

if __name__ == '__main__':
    app.run(debug=True)
