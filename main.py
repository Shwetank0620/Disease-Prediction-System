from diseasepredictionsystem.preprocess import load_data, preprocess
from diseasepredictionsystem.logging.logger import logging

print(">>>>>> Data Preprocessing Started <<<<<<")
logging.info("Data Preprocessing Pipeline Started")
path = 'data/raw'
data = load_data(path)
for name in data.keys():
    preprocess(df=data[name], file_name=name)
logging.info("Data Preprocessing Pipeline Completed")
print(">>>>>> Data Preprocessing Completed <<<<<<")