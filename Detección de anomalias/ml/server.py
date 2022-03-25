from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import json
import numpy as np
import math
from ModelPrediction import ModelPredicition 




app = Flask(__name__)
CORS(app)
@app.route('/api/healthcheck',methods=['GET'])
def healthcheck():
    
    data ="OK"
    return Response(data)

@app.route('/api/test/headers',methods=['POST'])
def headers():
    # Get headers for payload
    headers = ['times_pregnant', 'glucose', 'blood_pressure', 'skin_fold_thick', 'serum_insuling', 'mass_index', 'diabetes_pedigree', 'age']

    payload = request.json['data']
    #prediction = model.predict([[np.array(data['exp'])]])
    #output = prediction[0]
    values = [float(i) for i in payload.split(',')]
    
    input_variables = pd.DataFrame([values],
                                columns=headers, 
                                dtype=float,
                                index=['input'])
    sr = pd.Series([19.5, 16.8, 22.78, 20.124, 18.1002]) 
    #return input_variables.to_json(orient='records')
    return input_variables.to_json(orient='records')


     

@app.route('/api/models/load',methods=['POST'])
def load():  
    model = request.json['model']
    modelPredicition = ModelPredicition()
    modelPredicition.loadModel(model)
    print('leido pikle')
    return "leido"

@app.route('/api/models/predict',methods=['POST'])
def predict():  
    client = request.json['client']
    product =request.json['product']
    payload = request.json['data']

    #leo la matriz para poder predecir
    data = pd.DataFrame(payload)
    print(data.columns)
    cols = ['week','product_id','week_item_quantity_lag_1','item_avg_price','date_item_avg_price','date_item_avg_price_lag_1','date_item_avg_price_lag_2','date_item_avg_price_lag_3','date_item_avg_price_lag_4','week_item_quantity']
    data = data[cols]
    print(data.head(5))
    #calculo
    price =  request.json['price']
    modelPredicition = ModelPredicition()
    dfResultados = modelPredicition.predict(client,product,price,data)
    
    return Response(dfResultados.to_json(orient='records'), mimetype='application/json')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug = True)