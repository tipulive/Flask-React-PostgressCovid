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



@app.route('/apidata')


def insert():
   conn = get_db_connection()
   cur = conn.cursor()
   try:
    
    

    page = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
    data=json.loads(page.content)
    for key, value in data.items():
        sql="""INSERT INTO books (title, author, pages_num, review)VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s) ON CONFLICT (lat,long) 
                DO UPDATE 
                    SET confirmed=%s,deaths=%s,country=%s,population=%s,sq_km_area=%s,life_expectancy=%s,continent=%s,abbreviation=%s,location=%s,iso=%s,capital_city=%s,updated=%s """
        val=(value["All"].get("confirmed","none"),
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
             value["All"].get("updated","none"),
             value["All"].get("confirmed","none"),
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
             value["All"].get("updated","none")
             )
        cur.execute(sql,val)

    conn.commit()

    cur.close()
    conn.close()
    return DisplayData()
   except:
     return DisplayData()
    

def DisplayData():
    conn = get_db_connection()
    cur = conn.cursor()
    CovidData=cur.execute('SELECT * FROM covids;')
    CovidData = cur.fetchall()
    
    cur.close()
    conn.close()
    return jsonify(CovidData)




        
   

if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug=True)
 