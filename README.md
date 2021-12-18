# 

<h1 align="center">
    AutomatEDA📊
</h1>

<p align="center">
  <strong>Demo:</strong><a target="_blank" href="https://share.streamlit.io/ruthgn/automateda/main/app.py">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" width="120px;" alt="Launch Streamlit Web App" />
  </a>
</p>

## About the app
This app is an automated exploratory data analysis (EDA) tool for tabular data. It also allows you to quickly locate variables with the most potential for prediction tasks using [mutual information](https://www.kaggle.com/ryanholbrook/mutual-information).

### Example Datasets
The app includes the following built-in data sets to demonstrate functionalies:
* [Automobile Data Set](https://www.kaggle.com/toramky/automobile-dataset)
* [Bank Marketing Data Set](https://www.kaggle.com/ruthgn/bank-marketing-data-set)
* [California Housing Data Set](https://www.kaggle.com/camnugent/california-housing-prices)

## Tech Stack
* Python
* [pandas_profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html)
* NumPy
* Pandas
* Scikit-Learn
* Streamlit

## Running the app locally
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