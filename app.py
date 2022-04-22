import os
import string

import psycopg2
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# establishes connection to DB
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='aircraft_db',
                            user='admin',
                            password='admin')
    return conn


# gets user entry from UI
def get_user_entry():
    return;


# takes in input_type: the data type of field entered (EX: Aircraft Registration Number) user input
# creates SQL query to send to index() which will query database
def user_entry_to_sql(input_type: string, user_input: string):
    sql_query: string  # string that will hold the SQL query
    if input_type == "Aircraft Registration":  # Input is entered into Aircraft Registration text field
        sql_query = "SELECT * FROM Incidents WHERE aircraft_reg_number=" + user_input
    elif input_type == "Event Date":  # Input is entered into Event Date text field
        sql_query = "SELECT * FROM Incidents WHERE event_date=" + user_input
    elif input_type == "NTSB Number":  # Input is entered into NTSB Number text field
        sql_query = "SELECT * FROM Incidents WHERE event_ntsb_number=" + user_input
    elif input_type == "Aircraft Make":  # Input is entered into Aircraft Make text field
        sql_query = "SELECT * FROM Incidents WHERE Incidents.aircraft_reg_number = " \
                    "Aircraft.aircraft_reg_number AND Aircraft.aircraft_make=" + user_input
    elif input_type == "Aircraft Model":  # Input is entered into Aircraft Model text field
        sql_query = "SELECT * FROM Incidents WHERE Incidents.aircraft_reg_number = " \
                    "Aircraft.aircraft_reg_number AND Aircraft.aircraft_model=" + user_input
    elif input_type == "Event Location":  # Input is entered into Event Location text field
        sql_query = "SELECT * FROM Incidents WHERE event_date=" + user_input
    elif input_type == "Event Severity":  # Input is entered into Event Severity text field
        sql_query = "SELECT * FROM Incidents WHERE event_severity=" + user_input
    elif input_type == "Aircraft Make & Aircraft Model":  # Input is entered as combo; aircraft make & model text fields
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE Incidents.aircraft_reg_number = " \
                    "Aircraft.aircraft_reg_number AND Aircraft.aircraft_model=" + user_input_split[0] + "AND " \
                    "Aircraft.aircraft_make=" + \
                    user_input_split[1]
    elif input_type == "Event Date & Event Location":  # Input is entered as combo; event date & location text fields
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE event_date=" + user_input_split[0] + " AND " \
                    "event_location=" + \
                    user_input_split[1]
    elif input_type == "Event Date & Aircraft Registration":
        # Input is entered as combo; event date & aircraft reg num text fields
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE event_date=" + user_input_split[0] + \
                    " AND aircraft_reg_number=" + user_input_split[1]
    elif input_type == "Event Date & NTSB Number":  # Input is entered as combo; event date & NTSB number text fields
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE event_date=" + user_input_split[0] + \
                    " AND event_ntsb_number=" + user_input_split[1]
    elif input_type == "Event Date & Aircraft Make":
        # Input is entered as combo; event date & aircraft make text fields
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE Incidents.aircraft_reg_number = Aircraft.aircraft_reg_number AND" \
                    " event_date=" + user_input_split[0] + \
                    " AND Aircraft.aircraft_make=" + user_input_split[1]
    elif input_type == "Event Date & Aircraft Model":
        # Input is entered as combo; event date & aircraft model fields
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE Incidents.aircraft_reg_number = Aircraft.aircraft_reg_number AND" \
                    " event_date=" + user_input_split[0] + \
                    " AND Aircraft.aircraft_model=" + user_input_split[1]
    elif input_type == "Event Date & Casualties":
        # Input is entered as combo; event date & casualties fields !!! NEED TO FIX THIS ONE !!!
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE Incidents.aircraft_reg_number = Aircraft.aircraft_reg_number AND" \
                    " event_date=" + user_input_split[0] + \
                    " AND Aircraft.aircraft_model=" + user_input_split[1]
    elif input_type == "Aircraft Registration & NTSB Number":
        # Input is entered as combo; aircraft reg num & NTSB num fields
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE aircraft_registration_num=" + user_input_split[0] + " AND " \
                    "event_ntsb_number=" + user_input_split[1]
    elif input_type == "Aircraft Registration & Event Location":
        # Input is entered as combo; aircraft reg num & event location fields
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE aircraft_registration_num=" + user_input_split[0] + " AND " \
                    "event_location=" + user_input_split[1]

    index(sql_query)

#this runs at the start of the program
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM Aircraft;')
    result = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', result=result)

# template for requesting user entered info and returning query result
@app.route("/countaircraft", methods=['POST'])
def countaircraft():
    aircraft_model = request.form["aircraft_model"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM Aircraft WHERE Aircraft.aircraft_model=\'' + aircraft_model + '\';')
    result = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", result=result)
    
# queries 
# Select aircraft with an incident on user date
@app.route("/aircraftIncidentOnDate", methods=['POST'])
def aircraftIncidentOnDate():
    incident_date = request.form["incident_date"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT Aircraft.aircraft_reg_number FROM Aircraft, Incidents WHERE Aircraft.aircraft_reg_number=Incidents.aircraft_reg_number AND Incidents.event_date=\'' + incident_date + '\';')
    resultQuery1 = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", resultQuery1=resultQuery1)
    
# Select all incidents by aircraft model
@app.route("/incidentsByModel", methods=['POST'])
def incidentsByModel():
    aircraft_model2 = request.form["aircraft_model2"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT Incidents.event_ntsb_number FROM Aircraft, Incidents WHERE Aircraft.aircraft_reg_number=Incidents.aircraft_reg_number AND Aircraft.aircraft_model=\'' + aircraft_model2 + '\';')
    resultQuery2 = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", resultQuery2=resultQuery2)

# Insert an aircraft
@app.route("/insertAircraft", methods=['POST'])
def insertAircraft():
    aircraft_model_insert = request.form["aircraft_model_insert"]
    aircraft_make_insert = request.form["aircraft_make_insert"]
    aircraft_reg_num_insert = request.form["aircraft_reg_num_insert"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO Aircraft VALUES (' + aircraft_reg_num_insert + ', NULL, \'' + aircraft_make_insert + '\', \'' + aircraft_model_insert + '\'); SELECT * FROM Aircraft WHERE aircraft_reg_number=\'' + aircraft_reg_num_insert + '\';')
    result_insert = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", result_insert=result_insert)


