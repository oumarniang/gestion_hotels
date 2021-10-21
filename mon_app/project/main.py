# main.py

from flask import Blueprint, render_template, request, Flask,redirect, url_for, session
from flask_login import login_required, current_user
import sqlite3 as sql
import pickle
import requests
import json
import pandas as pd
# import numpy as np
import flask_monitoringdashboard as dashboard

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

    # fermeture connextion db
    conn.close()

    #  conversion json
    clients_json = json.dumps(result_data_list)

    return render_template('reservations.html', clients_test=result_data_list, clients_json=clients_json )

## Page de prédictions
@main.route('/processing', methods = ['POST', 'GET'])
@login_required
def processing():

    if request.method == "POST":
        # Reception data json 
        data_client_json=request.get_json()
        # infos_clients pour rappel affichage
        infos_client = data_client_json.copy()

        # suppression index
        del data_client_json['id']
        #  création dataframe individu à tester
        df_from_json = pd.DataFrame.from_dict([data_client_json])
        # print("df_from_json =", df_from_json)
        # print(df_from_json.columns)

        # ouverture modèle & prédiction
        model_pred = pickle.load(open('project/data/model.pkl','rb'))
        predict_result = model_pred.predict(df_from_json)
        if(predict_result == 0):
            prediction = "Risque d'annulation faible"
        else:
            prediction = "Risque d'annulation élevé"

        session['data_client'] = infos_client

        #  convert numpy int64 to python int
        pyval = predict_result[0].item()
        session['predict_result'] = pyval
        # print(predict_result[0])
        session['prediction'] = prediction

        return redirect(url_for('main.predictions'), code=302, Response=None)

    return "<p>Erreur POST data</p>"
    
## Page affichage prédictions
@main.route('/predictions')
@login_required
def predictions():
    data_client = session['data_client'] 
    predict_result = session['predict_result']      
    prediction = session['prediction']
    return render_template('predictions.html', data_client=data_client, predict_result=predict_result, prediction=prediction)

## Page Accueil
@main.route('/home')
def home():
    '''
        Page 'home'
        :return: render_template('home.html')
        :rtype: html page
    '''
    return render_template("home.html", tasks = tasks)