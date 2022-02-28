# Real Estate Price Prediction: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Future scope of project](#future-scope)


## Demo

### Website screenshot:
[![](/images/webpage_screencapture1.PNG)]

## Overview
This data science project walks through step by step process of how to build a real estate price prediction model and use it via a website.

We will first build a model using sklearn and linear regression using banglore home prices dataset from kaggle.com.

Second step would be to write a python flask server that uses the saved model to serve http requests.

Third component is the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price.

During model building we will cover almost all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc.


Technology and tools wise this project covers:
- Python
- Numpy and Pandas for data wrangling
- Matplotlib for data visualization
- Sklearn for model building.
- Jupyter notebook, Visual Studio code and pycharm as IDE
- Python flask for http server
- HTML/CSS/Javascript for UI.

## Installation
The Code is written in Python 3.9.10 If you don't have Python installed you can find it [here](https://www.python.org/downloads/). To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
## Directory Tree 
```
├── static 
│   ├── main.js
│   ├── css
│   	├── Styles.css
│   	├── bg.JPG
├── artifacts 
│   ├── columns.json
│   ├── house_price_model.pickle
├── training_code 
│   ├── Bengaluru_House_Data.csv
│   ├── columns.json
│   ├── House Prediction.ipyn
│   ├── house_price_model.pickle
├── template
│   ├── index.html
├── images
│   ├── webpage_screencapture1.png
│   ├── webpage_screencapture2.png
├── README.md
├── app.py
├── util.py
├── requirements.txt
```

## Future Scope

* Optimize Flask app.py
* Front-End 