import os
from dotenv import load_dotenv,find_dotenv
import psycopg2


load_dotenv(find_dotenv())



conn = psycopg2.connect(
        host=os.getenv('DB_HOST'), 
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'))

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS covids;')
cur.execute('CREATE TABLE covids (id serial PRIMARY KEY,'
                                 'confirmed varchar (150) NULL,'
                                 'deaths varchar (150) NULL,'
                                 'country varchar (150) NULL,'
                                 'population varchar (150) NULL,'
                                 'sq_km_area varchar (150) NULL,'
                                 'life_expectancy varchar (150) NULL,'
                                 'elevation_in_meters varchar (150) NULL,'
                                 'continent varchar (150) NULL,'
                                 'abbreviation varchar (150) NULL,'
                                 'location varchar (150) NULL,'
                                 'iso varchar (150) NULL,'
                                 'capital_city varchar (150) NULL,'
                                 'lat varchar (150) unique,'
                                 'long varchar (150) unique,'
                                 'updated varchar (191) NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP,'
                                 'CONSTRAINT com UNIQUE (lat,long));'
                                 )

# Insert data into the table



conn.commit()

cur.close()
conn.close()
