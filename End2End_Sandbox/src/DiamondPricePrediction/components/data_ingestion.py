'''
Code for modularising data ingestion.
'''

import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

class DataIngestionConfig:
    raw_data : str=os.path.join("artifacts", "raw.csv")
    train_data : str=os.path.join("artifacts", "train.csv")
    test_data : str=os.path.join("artifacts", "test.csv")

class Data_Ingestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def init_data_ingestion(self):
        logging.info("Data ingestion started...")
        
        try:
            data=pd.read_csv(Path(os.join("notebook/data", "gemstone.csv")))
            logging.info("I have set the dataset as - data")
            
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data, index=False)
            
            logging.info("I have saved Raw Dataset in artifact dir....")
            logging.info("Here I have performed train test split...")
            
            train_, test_ = train_test_split(data, test_size=0.3)
            logging.info("Training and test data is split (1:3)....")
            
            train_.to_csv(self.ingestion_config.train_data, index=False)
            test_.to_csv(self.ingestion_config.test_data, index=False)
            
            logging.info("Data Ingestion part completed")
            
            return (self.ingestion_config.train_data, 
                    self.ingestion_config.test_data)
            
        except Exception as e:
            logging.info("Exception during occured at data ingestion stage...")
            raise CustomException(e, sys)
    