import os
import string

import psycopg2
from flask import Flask, render_template

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
    if input_type == "Registration Number":
        sql_query = "SELECT * FROM Incidents WHERE aircraft_reg_number=" + user_input
    elif input_type == "Event Date":
        sql_query = "SELECT * FROM Incidents WHERE event_date=" + user_input
    elif input_type == "NTSB Number":
        sql_query = "SELECT * FROM Incidents WHERE event_ntsb_number=" + user_input
    elif input_type == "Aircraft Make":
        sql_query = "SELECT * FROM Incidents WHERE Incidents.aircraft_reg_number = " \
                    "Incidents.aircraft_reg_number AND Aircraft.aircraft_make=" + user_input
    elif input_type == "Aircraft Model":
        sql_query = "SELECT * FROM Incidents WHERE Incidents.aircraft_reg_number = " \
                    "Incidents.aircraft_reg_number AND Aircraft.aircraft_model=" + user_input
    elif input_type == "Event Location":
        sql_query = "SELECT * FROM Incidents WHERE event_date=" + user_input
    elif input_type == "Event Severity":
        sql_query = "SELECT * FROM Incidents WHERE event_severity=" + user_input
    elif input_type == "Aircraft Make & Aircraft Model":
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE Incidents.aircraft_reg_number = " \
                    "Incidents.aircraft_reg_number AND Aircraft.aircraft_model=" + user_input_split[0] + "AND " \
                    "Aircraft.aircraft_make=" + user_input_split[1]
    elif input_type == "Event Date & Event Location":
        user_input_split = user_input.split(" ")
        sql_query = "SELECT * FROM Incidents WHERE event_date=" + user_input_split[0] + " AND " \
            "event_location=" + user_input_split[1]

    index(sql_query)


@app.route('/')
def index(query: string):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', result=result)


"""
Example of pulling data from html page
@app.route("/personadd", methods=['POST'])
def personadd():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")
"""
