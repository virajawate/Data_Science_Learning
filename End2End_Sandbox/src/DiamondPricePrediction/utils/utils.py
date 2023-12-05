import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

from sklearn.metrics import r2_score

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)

def Evaluate_model(x_train, x_test, y_train, y_test, models):
    try:
        report_r2 = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(x_train, y_train)                           # Train model
            y_pred = model.predict(x_test)                        # Predict Testing data
            model_test_score = r2_score(y_test, y_pred)           # Get R2 score for test data
            report_r2[list(models.keys())[i]] = model_test_score  # Storing the score with model name in Dictionary
        return report_r2
    
    except Exception as e:
        logging.info("Exception occured during model training.")
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info("Exception occured in load_object function (utils)")
        raise CustomException(e, sys)
