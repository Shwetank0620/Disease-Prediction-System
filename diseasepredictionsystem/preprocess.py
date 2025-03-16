import pandas as pd
import glob
from diseasepredictionsystem.logging.logger import logging
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

def load_data(file_paths: str):
    csv_files = glob.glob(f'{file_paths}/*.csv')
    dfs = {}
    for file in csv_files:
        file_name = file.split("\\")[-1].split(".")[0]
        dfs[file_name] = pd.read_csv(file)
        logging.info(f"{file_name} Data File Loaded Successfully")
    return dfs

def preprocess(df: pd.DataFrame, file_name: str) -> None:
    if (len(df) - len(df.dropna())) > (0.1*len(df)):
        df.fillna(df.mean())
    else:
        df.dropna(inplace=True)
    
    categorical_cols = df.select_dtypes(include=["object"]).columns
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(categorical_cols) > 0:
        encoder = OneHotEncoder(sparse_output=False, drop="first")
        encoded_df = pd.DataFrame(encoder.fit_transform(df[categorical_cols]))
        encoded_df.columns = encoder.get_feature_names_out(categorical_cols)

        df = df.drop(columns=categorical_cols)
        df = pd.concat([df, encoded_df], axis=1)
    
    if len(numerical_cols) > 0:
        scaler = MinMaxScaler()
        df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    df.to_csv(f"data/processed/{file_name}.csv")

    logging.info(f"{file_name} Data File Preprocessed Successfully")