from datetime import datetime
import numpy as np
import pandas as pd
import math
from pandas import read_csv
from pandas import set_option
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import pickle

class ModelGenerator:
    def evaluate(self, model, test_features, test_labels):
        predictions = model.predict(test_features)
        errors = abs(predictions - test_labels)
        mape = 100 * np.mean(errors / test_labels)
        accuracy = 100 - mape
        return accuracy

    def create(self, client,product,matrix):
        # Tune scaled GBM
        validation_size = 0.20
        num_folds = 10
        seed = 7
        scoring = 'neg_mean_squared_error'

        array = matrix.values
        X = array[:,0:len(matrix.columns)-1]
        Y = array[:,(len(matrix.columns)-1)]
        X_train, X_valid, Y_train, Y_valid = train_test_split(X, Y, test_size=validation_size, random_state=seed)


        param_grid = dict(n_estimators=np.array([1,10,20,25,30,40,50,100,150,200,250,300,350,400]))
        model = GradientBoostingRegressor(random_state=seed,n_estimators=400)
        kfold = KFold(n_splits=num_folds, random_state=seed)
        grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
        grid_result = grid.fit(X_train, Y_train)



        best_GBR = grid_result.best_estimator_
        trained_model = pickle.dumps(best_GBR)
        #joblib.dump(best_GBR, 'c:/aplica/smartpricing/ML/best_gbr.lib')
        filename = 'best_gbr_'+str(client)+'_'+str(product)+'.pickle'
        pickle.dump(grid_result, open(filename, 'wb'))
        accuracy = str(self.evaluate(best_GBR,X_valid,Y_valid))
        print('accuracy '+ accuracy)
        modelResult = {
                        "accuracy":accuracy,
                         "model":filename
                        }
        return modelResult
