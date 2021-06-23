
from flask import Flask, request, render_template

import numpy as np

import re

import requests


app = Flask(__name__)


def check(output):

    url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"
    
    querystring = {"image_url":output,"sourceType":"url"}
    
    payload = '''{\r\n    \"image_url\": "'''+output+'''" ,\r\n    \"sourceType\": \"url\"\r\n}'''
    headers = {
    'x-rapidapi-key': "1684fa1d6dmsh60c658802264812p1b0bf3jsn58757764e534",  
    'x-rapidapi-host': "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com"
    }
    
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text) 
    return response.json()["results"][0]["plate"],response.json()["results"][0]["confidence"]
    
 

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/predict',methods=['POST'])
def predict():
    output=request.form['output']
    plate,conf=check(output)
    return render_template('base.html',output=plate+" with confidence score: "+str(round(conf))+"%")

    
if __name__ == "__main__":
    app.run(debug=True)
