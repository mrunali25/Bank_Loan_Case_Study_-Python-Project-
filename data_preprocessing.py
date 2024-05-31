# data_preprocessing.py
import pandas as pd
import numpy as np

def handle_missing_values(df):
    """
    Handle missing values in the DataFrame.
    """
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            df[column].fillna(df[column].mean(), inplace=True)
    return df

# Other functions for data cleaning can be added here if needed.
