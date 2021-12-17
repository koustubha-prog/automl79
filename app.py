import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression
from sklearn.feature_selection import mutual_info_classif
from pandas_profiling import ProfileReport
from pathlib import Path
import streamlit as st
from streamlit_pandas_profiling import st_profile_report


CHART_EMOJI_URL = "https://img.charactermap.one/google/android-11/512px/1f4ca.png"

# Set page title and favicon.
st.set_page_config(
    page_title="AutomatEDA", page_icon=CHART_EMOJI_URL,
)

########## Main Panel ##########

# Header and Description
st.write("""
# AutomatEDA📊 

An automated exploratory data analysis (EDA) tool for tabular data.

""")

st.caption("by [Ruth G. N.](https://www.linkedin.com/in/ruthgn/)")

"""
[![Follow](https://img.shields.io/twitter/follow/RuthInData?style=social)](https://www.twitter.com/RuthInData)
&nbsp[![Star](https://img.shields.io/github/stars/ruthgn/AutomatEDA.svg?logo=github&style=social)](https://github.com/ruthgn/AutomatEDA/stargazers)
&nbsp[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/ruthgn)
"""

########## ---------- ##########

def get_report(data=None):
    report = ProfileReport(data, explorative=True)
    return st_profile_report(report)


# Input data section
st.sidebar.header('Input Data')
st.sidebar.markdown("\n")
data = None

# Select data source
data_source = st.sidebar.radio("Select data source", ["Upload CSV file", "Use an example data set"])


if data_source == "Upload CSV file":
    # Upload csv file
    st.sidebar.markdown('***Upload your CSV file***:')
    uploaded_file = st.sidebar.file_uploader("📁⬇️",type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.success('File uploaded successfully.')
    else:
        st.info('Waiting for CSV file to be uploaded.')


else:
    # Select an example dataset (instead of uploading a file)    
    st.sidebar.markdown("\n")
    
    # Example datasets
    selected_example = st.sidebar.selectbox(label="Select example data set:", options=['Automobile Data Set', 'Bank Marketing Data Set', 'California Housing Data Set'])
    
    data_dir = Path("Example Datasets/")
    if selected_example == 'Automobile Data Set':
        data = pd.read_csv(data_dir / "automobile.csv")
        st.success('Automobile Data Set selected.')
    elif selected_example == 'Bank Marketing Data Set':
        data = pd.read_csv(data_dir / "bank-marketing.csv")
        st.success('Bank Marketing Data Set selected.')
    elif selected_example == 'California Housing Data Set':
        data = pd.read_csv(data_dir / "california-housing.csv")
        st.success('California Housing Data Set selected.')
    # Blank state (no data uploaded or selected)
    else:
        st.info('Awaiting for CSV file to be uploaded.')
        st.write('---')


# Analysis section
if data is not None:
    # Display data
    st.header('Data Set Preview')
    st.write(data)
    st.write('---')

    # Pandas Profiling Report / EDA
    st.header('Exploratory Data Analysis')
    st.markdown("\n")
    start_analysis = st.button('Get Report 🕵️')

    if start_analysis:
        get_report(data)
    else:
        st.info('Waiting for analysis to start.')


# Whether to include feature utility metric (optional)
st.sidebar.write('---')
is_for_prediction = st.sidebar.checkbox("Data set includes a target variable")


# Preparation to get MI scores (if applicable)
if is_for_prediction:

    if data is not None:
        st.write('---')
        st.header('Variable Importance Ranking')
        st.caption('Based on calculated [Mutual Information Scores](https://www.kaggle.com/ryanholbrook/mutual-information)')
        st.markdown("\n")


        # Select target variable
        select_target_var = st.sidebar.selectbox("What is the target variable?", data.columns)
        st.markdown("\n")

        # Target variable type
        target_var_type = st.sidebar.radio("What is the target variable type?", ['Numeric', 'Categorical'])


        # Remove rows with missing target values
        cleaned_data = data.dropna(axis=0, subset=[select_target_var])
        total_nulls = data[select_target_var].isnull().sum().sum()

        # Select variables to exclude (optional)
        removed_features = st.sidebar.multiselect("(Optional) Select variables to exclude when predicting target:", data.drop(select_target_var, axis=1).columns)
        st.sidebar.markdown("\n")
        if removed_features is not None:
            features = cleaned_data.drop(select_target_var, axis=1).drop(removed_features, axis=1)
        else:
            features = cleaned_data.drop(select_target_var, axis=1)
        # Remove rows with missing variable values
        total_nulls += features.isnull().sum().sum()
        features = features.dropna(axis=0)
        target_var = data[select_target_var].iloc[features.index]
  
        
        # Report target variable and the data type
        st.write(f"Prediction target: `{select_target_var}` (*{target_var_type}*).")


        def make_mi_scores(X, y):
            X = X.copy()
            # Label encoding for categorical variables
            for colname in X.select_dtypes(["object", "category"]):
                X[colname], _ = X[colname].factorize()
            # All discrete features should now have integer dtypes
            discrete_features = [pd.api.types.is_integer_dtype(t) for t in X.dtypes]
            if target_var_type == 'Categorical':
                y = y.factorize()[0]
                mi_scores = mutual_info_classif(X, y, discrete_features=discrete_features, random_state=0)
            else:
                mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features, random_state=0)
            mi_scores = pd.Series(mi_scores, name='MI Scores', index=X.columns)
            mi_scores = mi_scores.sort_values(ascending=False)
            return mi_scores

        def plot_mi_scores(scores): 
            scores = scores.sort_values(ascending=True)
            width = np.arange(len(scores))
            ticks = list(scores.index)
            fig = plt.figure(dpi=80, figsize=(6, 10))
            ax = fig.add_subplot()
            ax.barh(width, scores)
            ax.set_yticks(width, ticks)
            ax.set_title("Feature Utility Score")
            return fig


        # Get MI scores
        show_mi_scores = st.checkbox("Show variable importance ranking 🔎")

        # Report dropped rows
        if total_nulls > 0:
            st.warning(f"Removed {total_nulls} rows with missing values.")
        else:
            pass  

        # Display Feature Importance Report (if applicable)
        if show_mi_scores:
            # Get feature utility scores
            mi_scores = make_mi_scores(features, target_var)

            # Show Mutual Information (MI) score plot
            st.pyplot(plot_mi_scores(mi_scores), bbox_inches='tight')

        else:
            st.markdown("\n")


st.write('---')  
st.caption("Ran into a bug or saw something that could be improved on the app? Submit a [Github issue](https://github.com/ruthgn/AutomatEDA/issues) or [fork the repository](https://github.com/forks/ruthgn/Beer-Recommender) to create a pull request].")
