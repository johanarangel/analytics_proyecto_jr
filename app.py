#!/usr/bin/env python
'''
Página principal [Proyecto Python: Data Analytics]
---------------------------
Autor: Johana Rangel
Version: 1.0

Descripcion:
Programa creado para predicir los posibles delitos que ocurren por barrio tomando como datos hora, mes, dia y barrio.
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.0"

import traceback
import os
import pickle
import numpy as np 
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import LabelEncoder

# Crear el server Flask
app = Flask(__name__)

model = pickle.load(open('delitos_model.pkl', 'rb'))
encoding_barrio = pickle.load(open('label_encoding_barrio.pkl', 'rb'))

@app.route("/")
def index():
    try:
        return render_template('index.html')

    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/predict", methods = ['POST'])
def predict(): 
    try: 
        if request.method == 'POST':
            hora = int(request.form.get('hora'))
            dia= int(request.form.get('dia'))
            mes = int(request.form.get('mes'))
            barrio = str(request.form.get('barrio'))

            barrio_numero = encoding_barrio.fit_transform([barrio])         
            
            features = [hora, dia, mes, barrio_numero]
            numpy_features = [np.array(features)]
            prediction = model.predict(numpy_features)
            
            return render_template('index.html', prediction_text = f'{prediction}')

    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    print('Proyecto Data Analytics Python!')
    #Lanzar server
    app.run(debug=True)
    