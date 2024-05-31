# streamlit_app.py
import streamlit as st
import pandas as pd
import data_preprocessing
import outlier_detection
import data_analysis
import visualization

def main():
    st.title("Loan Application Analysis Dashboard")

    # Load the data
    st.header("Loading Data...")
    df = pd.read_csv(r"Bank loan case study\application_data.csv")
    st.write("Data Loaded Successfully!")

    # Data Preprocessing
    st.header("Data Preprocessing")
    st.subheader("Handling Missing Values")
    df_cleaned = data_preprocessing.handle_missing_values(df)
    st.write("Missing Values Handled")
    st.write("Head of Cleaned Data:")
    st.write(df_cleaned.head())

    # Outlier Detection
    st.header("Outlier Detection")
    st.subheader("Handling Outliers")
    df_cleaned = outlier_detection.handle_outliers(df_cleaned)
    st.write("Outliers Detected and Handled")
    st.write("Head of Data after Outlier Handling:")
    st.write(df_cleaned.head())

    # Data Analysis
    st.header("Data Analysis")
    st.subheader("Univariate Analysis")
    st.write("Performing Univariate Analysis...")
    columns_of_interest = ['TARGET', 'NAME_CONTRACT_TYPE', 'CODE_GENDER', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'OCCUPATION_TYPE']
    data_analysis.perform_univariate_analysis(df_cleaned, columns_of_interest)
    st.write("Univariate Analysis Completed!")

    st.subheader("Segmented Univariate Analysis")
    st.write("Performing Segmented Univariate Analysis...")
    numerical_columns_for_segment = ['NAME_CONTRACT_TYPE', 'CODE_GENDER', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'OCCUPATION_TYPE']
    data_analysis.perform_segmented_univariate_analysis(df_cleaned, numerical_columns_for_segment)
    st.write("Segmented Univariate Analysis Completed!")

    st.subheader("Bivariate Analysis")
    st.write("Performing Bivariate Analysis...")
    data_analysis.perform_bivariate_analysis(df_cleaned, columns_of_interest)
    st.write("Bivariate Analysis Completed!")

    # Visualization
    st.header("Visualization")
    image = visualization.plot_all_visualizations(df_cleaned)
    st.image(image)

if __name__ == "__main__":
    main()
