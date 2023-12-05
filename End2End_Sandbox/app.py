import os, sys
import pandas as pd
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.utils.utils import load_object

class Predict_pipeline:
    def __init__(self) -> None:
        pass
    
    def Predict(self, features):
        try:
            preprocessor_path = os.path.join("aritfacts", "preprocessor.pkl")
            model_path = os.path.join("aritfacts", "model.pkl")
            
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)
            
            scaledData = preprocessor.transform(features)
            
            pred = model.predict(scaledData)
            
            return pred
        
        except Exception as e:
            raise CustomException(e, sys)            