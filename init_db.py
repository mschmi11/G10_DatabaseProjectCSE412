import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="aircraft_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Aircraft;')
cur.execute('DROP TABLE IF EXISTS Casualties;')
cur.execute('DROP TABLE IF EXISTS Incidents;')

cur.execute('CREATE TABLE Aircraft(aircraft_reg_number varchar(255),'
            'event_ntsb_number varchar(255),'
            'aircraft_make varchar(255),'
            'aircraft_model varchar(255),'
            'PRIMARY KEY (aircraft_reg_number));'
            )

cur.execute('CREATE TABLE Casualties(casualty_id varchar(255),'
            'event_ntsb_number varchar(255),'
            'first_name varchar(255),'
            'last_name varchar(255),'
            'dob varchar(255),'
            'age int,'
            'sex varchar(20),'
            'PRIMARY KEY (casualty_id));'
            )

cur.execute('CREATE TABLE Incidents(event_ntsb_number varchar(255),'
            'aircraft_reg_number varchar(255),'
            'event_severity varchar(255),'
            'event_date varchar(255),'
            'event_location varchar(255),'
            'PRIMARY KEY (event_ntsb_number),'
            'FOREIGN KEY (aircraft_reg_number) REFERENCES Aircraft(aircraft_reg_number));'
            )

cur.execute('ALTER TABLE Casualties ADD FOREIGN KEY (event_ntsb_number) REFERENCES Incidents(event_ntsb_number);')

cur.execute('ALTER TABLE Aircraft ADD FOREIGN KEY (event_ntsb_number) REFERENCES Incidents(event_ntsb_number);')

cur.execute('INSERT INTO Aircraft(aircraft_reg_number, aircraft_make, aircraft_model ) '
            'VALUES(%s,%s,%s)',
            ('vo0647',
             'Airbus',
             'A234')
            )

conn.commit()

cur.close()
conn.close()
