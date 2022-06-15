import os
import requests
from sqlite3 import Cursor
import psycopg2
import json
from flask import Flask,jsonify,request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
         host=os.getenv('DB_HOST'), 
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'))
    return conn

@app.route('/apitest')
def hello():
 conn = get_db_connection()
 cur = conn.cursor()
 CovidData=cur.execute('SELECT * FROM covids;')
 CovidData = cur.fetchall()
    
 cur.close()
 conn.close()
 return jsonify(CovidData)

@app.route('/insert')
def insert():
    conn = get_db_connection()
    cur = conn.cursor()
    page = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
    data=json.loads(page.content)
    for key, value in data.items():
        cur.execute('INSERT INTO covids(confirmed,deaths,country,population,sq_km_area,life_expectancy,elevation_in_meters,continent,abbreviation,location,iso,capital_city,lat,long,updated)'
            'VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)',
            (value["All"].get("confirmed","none"),
             value["All"].get("deaths","none"),
             value["All"].get("country","none"),
             value["All"].get("population","none"),
             value["All"].get("sq_km_area","none"),
             value["All"].get("life_expectancy","none"),
             value["All"].get("elevation_in_meters","none"),
             value["All"].get("continent","none"),
             value["All"].get("abbreviation","none"),
             value["All"].get("location","none"),
             value["All"].get("iso","none"),
             value["All"].get("capital_city","none"),
             value["All"].get("lat","none"),
             value["All"].get("long","none"),
             value["All"].get("updated","none")
             
            )
           )

    conn.commit()

    cur.close()
    conn.close()
    return 'ok'


@app.route('/api')
def api():
    page = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
    
  
    data=json.loads(page.content)
    mydata=[]
    
    for key, value in data.items():
    
        mydata.append(value["All"].get("continent","none"))
    
    return jsonify({'country': mydata})
        
   

if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug=True)
 