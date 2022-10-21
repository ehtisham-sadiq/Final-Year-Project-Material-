import json
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


if __name__ == '__main__':
    app.run(debug=True)