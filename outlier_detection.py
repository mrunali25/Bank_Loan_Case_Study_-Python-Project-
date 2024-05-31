# outlier_detection.py
import pandas as pd
import numpy as np

def identify_outliers(column):
    """
    Identify outliers in a column using IQR method.
    """
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    threshold = 1.5
    outliers = (column < Q1 - threshold * IQR) | (column > Q3 + threshold * IQR)
    return outliers

def handle_outliers(df):
    """
    Handle outliers in the DataFrame.
    """
    outliers_dict = {}
    for column in df.columns:
        if np.issubdtype(df[column].dtype, np.number):
            outliers_dict[column] = identify_outliers(df[column])

    # Handle outliers as per your requirement
    # For example, you can replace outliers with mean/median, or remove them.
    # df_cleaned = df[~outliers_dict.any(axis=1)]  # Remove rows with any outlier
    return df

# Other outlier handling functions can be added here if needed.
