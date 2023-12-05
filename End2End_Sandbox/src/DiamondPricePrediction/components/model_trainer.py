import os, sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.DiamondPricePrediction.utils.utils import save_obj
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.utils.utils import logging
from src.DiamondPricePrediction.utils.utils import Evaluate_model
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()
    
    def initate_model_training(self, train_arr, test_arr):
        try:
            print(train_arr.shape, test_arr.shape)
            logging.info("Splitting Dependent and Independent variables from train and test data...")
            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1], train_arr[:, -1],
                test_arr[:, :-1], test_arr[:, -1])
            print(x_train.shape, y_train.shape)
            models = {'Lasso':Lasso(), 'Ridge':Ridge(),
                'LinearRegression':LinearRegression(),
                'Elasticnet':ElasticNet()}
            model_report:dict = Evaluate_model(x_train, x_test, y_train, y_test, models)
            print(model_report)
            print('\n==================================================================================\n')
            logging.info(f'Model Report : {model_report}')
            best_model_score = max(sorted(model_report.values()))
            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[str(best_model_name)]

            print(f"Best Model Found, Model Name : {best_model_name}, R2 Score : {best_model_score}")
            print('\n===================================================================================\n')
            logging.info(f"Best Model Found, Model Name : {best_model_name}, R2 Score : {best_model_score}")
            
            save_obj(
                file_path = self.model_trainer_config.trained_model_path,
                obj = best_model
            )
            
        except Exception as e:
            logging.info('Exception occured at Model Training....')
            raise CustomException(e, sys)
