# Rossmann-Sales-Forecasting-ML
## Overview
This project aims to develop an end-to-end machine learning solution for forecasting daily sales at Rossmann Pharmaceuticals stores across multiple cities. The goal is to enable the finance team to predict sales up to six weeks in advance, leveraging various features such as promotions, holidays, and store types.

## Table of Contents
- [Project Structure](#project-structure)
- [Data Description](#data-description)
- [Installation](#installation)
- [Usage](#usage)
- [Modeling Approach](#modeling-approach)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

/RossmannSalesForecast
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── data/ # Data files
├── src/
│   ├── __init__.py
├── notebooks/ # Jupyter notebooks for analysis and modeling
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/ # Source code for data processing and modeling
    ├── __init__.py
    └── README.md


## Data Description
The dataset is sourced from [Kaggle - Rossmann Store Sales](https://www.kaggle.com/c/rossmann-store-sales). It includes the following fields:

- **Id**: Unique identifier for each store and date.
- **Store**: Unique ID for each store.
- **Sales**: Daily sales turnover (target variable).
- **Customers**: Number of customers on a given day.
- **Open**: Indicator for whether the store was open (0 = closed, 1 = open).
- **StateHoliday**: Indicates if the day is a state holiday.
- **SchoolHoliday**: Indicates if schools were closed on that day.
- **StoreType**: Differentiates between four store models.
- **Assortment**: Describes the assortment level.
- **CompetitionDistance**: Distance to the nearest competitor.
- **Promo**: Indicates if a store is running a promotion.

## Installation
To run this project, clone the repository and install the required packages:

bash
git clone https://github.com/Ermi23/Rossmann-Sales-Forecasting-ML.git
cd RossmannSalesForecast
pip install -r requirements.txt
Usage
Data Exploration: Open the Jupyter notebooks in the notebooks/ directory to explore customer purchasing behavior and visualize relevant data.
Model Training: Run the scripts in the src/ directory to preprocess the data and train the machine learning models.
Model Serving: Utilize the API to serve predictions in real-time.
Modeling Approach
Exploratory Data Analysis (EDA): Analyze customer behavior and relationships between features and sales.
Feature Engineering: Create new features from existing data to improve model performance.
Machine Learning Models: Implement various regression models using scikit-learn, including Random Forest Regressor.
Deep Learning Models: Build an LSTM model for time series prediction using TensorFlow or PyTorch.
Results
The project aims to achieve accurate sales predictions, facilitating better planning for the finance team. Detailed performance metrics will be provided in the notebooks.
