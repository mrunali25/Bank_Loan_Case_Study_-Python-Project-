# data_analysis.py
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def perform_univariate_analysis(df, columns_of_interest):
    """
    Perform Univariate Analysis and return Matplotlib figures.
    """
    for column in columns_of_interest:
        plt.figure(figsize=(8, 5))
        if df[column].dtype == 'object':
            # For categorical variables, create a bar plot
            sns.countplot(x=column, data=df)
        else:
            # For numerical variables, create a histogram
            sns.histplot(df[column], bins=20, kde=True)
        plt.title(f'Distribution of {column}')
        # Save the Matplotlib figure and return it
        st.pyplot(plt)

def perform_segmented_univariate_analysis(df, numerical_columns_for_segment):
    """
    Perform Segmented Univariate Analysis and return Matplotlib figures.
    """
    for column in numerical_columns_for_segment:
        plt.figure(figsize=(12, 6))
        sns.violinplot(x='TARGET', y=column, data=df, hue='TARGET', split=True)
        plt.title(f'{column} Distribution by Target')
        plt.xlabel('Target')
        plt.ylabel(column)
        # Save the Matplotlib figure and return it
        st.pyplot(plt)

def perform_bivariate_analysis(df, columns_of_interest):
    """
    Perform Bivariate Analysis and return Matplotlib figures.
    """
    for column in columns_of_interest[2:]:  # Skip the target and contract type variables for bivariate analysis
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=column, y='AMT_CREDIT', hue='TARGET', data=df)
        plt.title(f'Scatter Plot of {column} vs. AMT_CREDIT by Loan Status')
        plt.xlabel(column)
        plt.ylabel('AMT_CREDIT')
        # Save the Matplotlib figure and return it
        st.pyplot(plt)
