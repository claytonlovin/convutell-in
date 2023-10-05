from flask import Flask, render_template, request, redirect, url_for

from datetime import datetime
from decouple import config 
import requests

app  = Flask(__name__,
template_folder="../templates",
static_folder="../static")




# DEFINIR URL
API_URL = config('API_URL')

   
if __name__ == '__main__':
    app.run(debug=True)
