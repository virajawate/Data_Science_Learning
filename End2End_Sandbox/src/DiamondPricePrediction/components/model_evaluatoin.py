import os, sys
import numpy as np
import pickle
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse
from src.DiamondPricePrediction.utils.utils import load_object
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class ModelEvaluation:
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def initiate_model_evaluation(self, train_a, test_a):
        try:
            x_test, y_test = (test_a[:, :-1], test_a[:, -1])
            
            model_path = os.path.join("artifacts", "model.pkl")
            model = load_object(model_path)

            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            print(tracking_url_type_store)
            
            with mlflow.start_run():
                y_pred = model.predict(x_test)
                (rmse, mae, r2) = self.eval_metrics(y_test, y_pred)
                
                mlflow.log_metric('rmse', rmse)
                mlflow.log_metric('mae', mae)
                mlflow.log_metric('r2', r2)
                
                if tracking_url_type_store != 'file':
                    mlflow.sklearn.log_model(model, "model", registered_model_name='ml_model')
                else:
                    mlflow.sklearn.log_model(model, 'model')
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e