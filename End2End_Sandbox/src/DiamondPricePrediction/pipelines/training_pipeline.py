import os, sys
import pandas as pd
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.components.model_trainer import ModelTrainer
from src.DiamondPricePrediction.components.model_evaluatoin import ModelEvaluation
from src.DiamondPricePrediction.components.data_ingestion import Data_Ingestion
from src.DiamondPricePrediction.components.data_transformation import Data_Transformation

obj = Data_Ingestion()
train_data_path, test_data_path = obj.init_data_ingestion()

data_transformation = Data_Transformation()
train_a, test_a = data_transformation.initialize_data_transformation(train_data_path, test_data_path)

model_trainer_obj = ModelTrainer()
model_trainer_obj.initate_model_training(train_a, test_a)

model_eval_obj = ModelEvaluation()
model_eval_obj.initiate_model_evaluation(train_a, test_a)
