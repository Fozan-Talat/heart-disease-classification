# Heart Disease Risk Classification

Here you'll find a solution to selecting and training a classification model to predict the risk for heart disease, putting it into a web service using [Flask](https://flask.palletsprojects.com/en/3.0.x/) and then containerizing it using docker.

## The problem

The [risk for heart disease](https://www.cdc.gov/heartdisease/risk_factors.htm) can be associated with health conditions and factors such as lifestyle, age, and family history. A binary classification model based on these variables collected from patients can help in healthcare diagnosis.

## The data

A [reduced version](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease) of the [CDC](https://www.cdc.gov/) dataset (February 2022 update) containing several features that can be associated with the risk of heart disease is used to build the classification model. Reduced here means that the 300 variables from the original dataset were reduced to 20. 

The imbalanced data consists of 17 attributes and one target variable `heart_disease`.

## The model

The best model was XGBOOST selected from the following:
* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost


First baseline models were obtained without handling the class imbalance, and then new models were built handling class imbalance with class weights. Techniques like oversampling and/or undersampling were not applied here.

## The metrics

Several metrics were calculated but the most useful for this problem were **F1**, **recall**, and **MCC** (Matthews correlation coefficient).

## How to run this project

* Create a virtual environment of your choice using (Pipenv,conda,venv) and activate it
* Clone this repository
* Install project dependencies: 
```bash
 pip install -r requirements.txt 
```

* Inside the repository create a new directory called `data` and manually download this [Kaggle](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease) dataset to it.
* Run and inspect Notebook.ipynb 
* The best model is saved using pickle. From here you will need the file `web_service.py`.
If you want to run the container, run:
```bash
$ docker run -it --rm -p 7860:7860 web_service
```
and access the given local address to use it.

if you want to just run the flask api , run the following command in cli
```
python web_service.py
```



