from diseasepredictionsystem.preprocess import preprocess
from diseasepredictionsystem.train import train
from diseasepredictionsystem.utils.main_utils.utils import load_data
from diseasepredictionsystem.logging.logger import logging

print(">>>>>> Data Preprocessing Started <<<<<<")
logging.info("Data Preprocessing Pipeline Started")
path = 'data/raw'
data = load_data(path)
for name in data.keys():
    preprocess(df=data[name], file_name=name)
logging.info("Data Preprocessing Pipeline Completed")
print(">>>>>> Data Preprocessing Completed <<<<<<")

print(">>>>>> Model Training Started <<<<<<")
logging.info("Model Training Pipeline Started")
path = 'data/processed'
data = load_data(path)
for name in data.keys():
    train(df=data[name], file_name=name)
logging.info("Model Training Pipeline Completed")
print(">>>>>> Model Training Completed <<<<<<")