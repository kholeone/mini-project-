from flask import render_template
from application import app
import requests

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title='Home')

@app.route('/get/animal', methods = ['GET', 'POST'])
def animal():
    animal = requests.get('http://service-2:5001/animal/name')
    noise = requests.post('http://service2:5001/animal/noise', data=animal.text)
    return render_template('animals.html', title='Animals', animal=animal.text, noise=noise.text)
