import pandas as pd
from flask import *
import mysql.connector as con
import pymongo


app = Flask(__name__)




@app.route("/xn",methods = ['GET',"POST"])
def rutvik():
    try:
        if request.method=='POST':
            a = request.json['num2']
            b = request.json['num1']
            return jsonify({str(a+b):"Rutvik_Jaiswal"})

    except Exception as e:
        return e

@app.route("/show_data/",methods = ['GET',"POST"])
def dataframe():
    try:
        if request.method=='GET':
            df  = pd.read_csv('data_by_year.csv')
            table = df.to_html(header="true", table_id="table")
            return table
    except Exception as e:
        return e


@app.route("/show_sql/",methods = ['GET',"POST"])
def sql_data():
    try:
        if request.method=='GET':
            connect = con.connect(host = 'localhost',user = 'root',passwd = 'ru15070610',  database = 'glass_set')
            df  = pd.read_sql("select * from glass_value limit 10",connect)
            table = df.to_html(header="true", table_id="table")
            return table
    except Exception as e:
        return e



@app.route("/see_mongoDB")
def home():
    client = pymongo.MongoClient(
    "mongodb+srv://mongodb:ru15070610@cluster0.4olre.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    absc =client['first_database']['first']

    data = pd.DataFrame(list(absc.find()))


    return data.to_html(header="true", table_id="table")



if __name__=="__main__":
    app.run(debug=True)