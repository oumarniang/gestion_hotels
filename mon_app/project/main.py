# main.py

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import sqlite3 as sql
import pickle
import requests
import json
import pandas as pd
import ast

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

## Page de Bienvenue
@main.route('/bienvenue')
@login_required
def bienvenue():
    return render_template('reservations.html')

## Page de réservations
@main.route('/reservations')
@login_required
def reservations():
    conn = sql.connect('project/data/hotel.db')

    #  get columns names from table
    cur1 = conn.cursor()
    cur1.execute("SELECT * FROM PRAGMA_TABLE_INFO('hotel')")
    result_columns = cur1.fetchall()
    #  remove first element from list
    del result_columns[0]
    #  create columns_names list
    columns_names = []
    for item in result_columns:
        column_name = list(item)[1]
        columns_names.append(column_name)

    # data query
    cur2 = conn.cursor()
    cur2.execute('SELECT * FROM hotel WHERE arrival_date_year="2015" LIMIT 20')
    result_query = cur2.fetchall()
    result_data_list = []
    for item in result_query:
        item_list = list(item)
        del item_list[0]
        #  zip
        item_zipped = zip(columns_names, item_list)
        item_dict = dict(item_zipped)
        # print(item_dict)
        result_data_list.append(item_dict)

    # create result dictionnary
    # print(result_data_list)
    conn.close()

    return render_template('reservations.html', clients_test=result_data_list )
 

## Page de prédictions
@main.route('/predictions/<data_client>', methods = ['POST', 'GET'])
@login_required
def predictions(data_client):
    
    sample = ast.literal_eval(data_client)
    del sample['id']
    # print(sample)
    df = pd.DataFrame.from_dict([sample])
    print(df)

    model_pred = pickle.load(open('project/data/model.pkl','rb'))
    predict_result = model_pred.predict(df)

    return render_template('predictions.html', data_client=data_client, predict_result=predict_result[0])


## Page Accueil
@main.route('/home')
def home():
    '''
        Page 'home'
        :return: render_template('home.html')
        :rtype: html page
    '''
    return render_template("home.html", tasks = tasks)
