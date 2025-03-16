from diseasepredictionsystem.logging.logger import logging
from diseasepredictionsystem.exception.exception import DiseasePredictionException
from diseasepredictionsystem.utils.main_utils.utils import load_data

import os
import sys
import pickle
from sklearn.linear_model import LogisticRegression

# import yaml

# params = yaml.safe_load('params.yaml')['train']
def train(df, file_name):
    try:
        X = df.drop(columns=['Outcome'])
        y = df['Outcome']
        
        lr = LogisticRegression()
        lr.fit(X, y)

        os.makedirs('Models', exist_ok=True)
        with open(f'Models/{file_name}.sav', 'wb') as f:
            pickle.dump(lr, f)
    except Exception as e:
        raise DiseasePredictionException(e, sys)