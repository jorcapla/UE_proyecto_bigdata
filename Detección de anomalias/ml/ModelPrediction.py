import pickle
import pandas as pd
import json
import numpy as np
import math

class ModelPredicition:
    def loadModel(self,model):
        #filename = 'best_gbr_'+str(client)+'_'+str(product)+'.pickle'
        filename = model+'.pickle'
        model = pickle.load(open(filename, 'rb'))
        model = model.best_estimator_
        print('leido pikle')
        return model
    def predict(self,model,data):
        #calculo
        dfResultados = data.copy()
        longitud=len(dfResultados.columns)
        anomaly_model = self.loadModel(model)
        
        df = dfResultados[['week','product_id','week_item_quantity','item_avg_price','predictionPrice','quantityPrediction','quantityPredictionReal']]
        df = df.rename(columns={'product_id': 'product','week_item_quantity': 'quantity',  'item_avg_price':'actualPrice'}) 
        return df
