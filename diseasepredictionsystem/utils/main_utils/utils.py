import glob
import pandas as pd
from diseasepredictionsystem.logging.logger import logging

def load_data(file_paths: str):
    csv_files = glob.glob(f'{file_paths}/*.csv')
    dfs = {}
    for file in csv_files:
        file_name = file.split("\\")[-1].split(".")[0]
        dfs[file_name] = pd.read_csv(file)
        logging.info(f"{file_name} Data File Loaded Successfully")
    return dfs