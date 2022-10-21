import json
import requests
import pickle
import re
import pandas as pd
import numpy as np
from flask import Flask, render_template, url_for,jsonify
import flask_monitoringdashboard as monitoring_dashboard

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = requests.json['data']
    #this is used to test our web application
    return jsonify(output)


@app.route('/predict', methods=['POST'])
def predict():
    data = requests.form.values()
    
    return render_template('home.html', prediction_text = "The Expected Salary of Software Developer is: {}".format(result))

if __name__ == '__main__':
    app.run(debug=True)