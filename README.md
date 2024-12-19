# Biochar-Yield-Prediction
## About
Biochar production via pyrolysis of organic waste is a sustainable process with significant potential to reduce reliance on conventional energy sources and mitigate global warming. Utilizing a given dataset containing input feedstock compositions and pyrolysis process conditions, this app's purpose is to use machine learning models to predict biochar yield.
## Usage
This app can be run through huggingface (https://huggingface.co/spaces/kaylayi18/BiocharYieldPrediction/tree/main). The required libraries are listed in the requirement.txt file. The user inputs various parameters and the model predicts the biochar yield from these inputs.
The user inputs are the following:
- Feedstock
- Feedstock Proximate Analysis - Fixed Carbon, Volatile Matter, Ash,
- Feedstock Ultimate Analysis - C, H, O, N
- Pylorosis Conditions - Residence Time, Temperature, Heating Rate

In order to deploy the app on huggingface yourself, please upload the bestmodel file, requirements, and app.py

## Description
This repository includes the data preprocessing in google colab and the best/trained machine learning model. The best model identified from training multiple machine learning models is Logistic Regression. The datasource for this project is included in the repository.

The ML model that was used to build this app is Logistic Regression. This model was chosen because over three evaluation metrics (RMSE, MAE and R^2), it performed the best. Out of the five ML models tested, it had the lowest RMSE, so taking all of these into account, Logistic Regression would provide the most accurate model. Logistic regression is a machine learning model best suited for binary classification problems. It provides a model that is easy to interpret and is useful for the size of the dataset.
