import os
import pandas as pd
from diseasepredictionsystem.logging.logger import logging
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def preprocess(df: pd.DataFrame, file_name: str) -> None:
    if (len(df) - len(df.dropna())) > (0.1 * len(df)):
        df.fillna(df.mean(), inplace=True)
    else:
        df.dropna(inplace=True)
    
    categorical_cols = df.select_dtypes(include=["object"]).columns

    for col in categorical_cols:
        unique_vals = df[col].nunique()
        
        if unique_vals == 2:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col]) 
        else:
            encoder = OneHotEncoder(sparse_output=False, drop="first")
            encoded_array = encoder.fit_transform(df[[col]])

            encoded_col_names = [f"{col}_{category}" for category in encoder.categories_[0][1:]]

            encoded_df = pd.DataFrame(encoded_array, columns=encoded_col_names, index=df.index)

            df = df.drop(columns=[col])
            df = pd.concat([df, encoded_df], axis=1)
    
    os.makedirs("data/processed", exist_ok=True)
    
    df.to_csv(f"data/processed/{file_name}.csv", index=False)

    logging.info(f"{file_name} Data File Preprocessed Successfully")