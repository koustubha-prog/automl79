# 

<h1 align="center">
    AutomatEDA📊
</h1>

<p align="center">
  <a target="_blank" href="https://share.streamlit.io/ruthgn/automateda/main/app.py">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" width="170px;" alt="Launch Streamlit Web App" />
  </a>
</p>


## About The App
This app is an automated exploratory data analysis (EDA) tool for tabular data. Simply upload your CSV file and explore your data with *one click*—all the following variable information will be generated in an interactive HTML report (if relevant for the variable/column type):
* **Type inference** detecting the types of columns in the file (dataframe)
* **Essentials**: data type, unique values, missing values
* **Quantile statistics**: minimum value, Q1, median, Q3, maximum, range, interquartile range
* **Descriptive statistics**: mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
* **Most frequent values**
* **Histogram**
* **Correlations** highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices
* **Missing values** matrix, count, heatmap and dendrogram of missing values
* **Text analysis** to learn about categories (Uppercase, Space), scripts (Latin, Cyrillic) and blocks (ASCII) of text data.
* **File analysis** to extract file sizes, creation dates and dimensions

Additionally, this app also allows you to quickly **locate variables with the most potential** for prediction tasks using [mutual information](https://www.kaggle.com/ryanholbrook/mutual-information).

### Example Datasets
The app includes the following built-in data sets to demonstrate functionalies:
* [Automobile Data Set](https://www.kaggle.com/toramky/automobile-dataset)
* [Bank Marketing Data Set](https://www.kaggle.com/ruthgn/bank-marketing-data-set)
* [California Housing Data Set](https://www.kaggle.com/camnugent/california-housing-prices)

## Screenshots
| ![screen-gif](assets/AutomatEDA-demo-screencast-1.gif) | 
|:--:| 
| *One-Click Exploratory Data Analysis* |

| ![screen-gif](assets/AutomatEDA-demo-screencast-2.gif) | 
|:--:| 
| *Generating Variable Importance Rankings* |

## Tech Stack
* Python
* NumPy
* pandas
* Matplotlib
* [pandas_profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html)
* scikit-learn
* Streamlit

## Running The App Locally
Open a command prompt in your chosen project directory. Create a virtual environment with conda, then activate it.
```
conda create -n myenv python=3.8.12
conda activate myenv
```

Clone this git repo, then install the specified requirements with pip.
```
git clone https://github.com/ruthgn/AutomatEDA
cd AutomatEDA
pip install -r requirements.txt
```

Run the app.
```
streamlit run app.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/ruthgn/AutomatEDA/blob/main/LICENSE) file for details.
