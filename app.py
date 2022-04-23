import os
import string

import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config["Our Database"] = where to get database
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)  # learns database tables, columns, types, etc


class Incidents(db.Model):  # creates class based on the Incidents' table of our DB
    __tablename__ = 'Incidents'
    __table_args__  = {'extend_existing': True}
    incident_key = db.Column(db.Text, primary_key=True)  # sets primary key of Incidents' table


class Aircraft(db.Model):  # creates class based on the Aircraft table of our DB
    __tablename__ = 'Aircraft'
    __table_args__  _args = {'extend_existing': True}
    aircraft_key = db.Column(db.Text, primary_key=True)  # sets primary key of Aircraft table


class Casualties(db.Model):  # creates class based on the Casualties' table of our DB
    __tablename__ = 'Casualties'
    __table_args__  = {'extend_existing': True}
    casualty_key = db.Column(db.Text, primary_key=True)  # sets primary key of Casualties' table


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
# creates SQL query through SQLAlchemy
def user_entry_to_sql(input_type: string, user_input: string):
    Session = sessionmaker(db.engine)
    session = Session()
    sql_query: string  # string that will hold the SQL query
    if input_type == "Aircraft Registration":  # Input is entered into Aircraft Registration text field
        sql_query = session.query(Incidents).filter(Incidents.aircraft_reg_number == user_input).all()
    elif input_type == "Event Date":  # Input is entered into Event Date text field
        sql_query = session.query(Incidents).filter(Incidents.event_date == user_input).all()
    elif input_type == "NTSB Number":  # Input is entered into NTSB Number text field
        sql_query = session.query(Incidents).filter(Incidents.event_ntsb_number == user_input)
    elif input_type == "Aircraft Make":  # Input is entered into Aircraft Make text field
        sql_query = session.query(Incidents).join(Aircraft).filter(Aircraft.aircraft_make == user_input).all()
    elif input_type == "Aircraft Model":  # Input is entered into Aircraft Model text field
        sql_query = session.query(Incidents).join(Aircraft).filter(Aircraft.aircraft_model == user_input).all()
    elif input_type == "Event Location":  # Input is entered into Event Location text field
        sql_query = Incidents.query.filter(Incidents.event_location == user_input).all()
    elif input_type == "Event Severity":  # Input is entered into Event Severity text field
        sql_query = Incidents.query.filter(Incidents.event_severity == user_input).all()
    elif input_type == "Aircraft Make & Aircraft Model":  # Input is entered as combo; aircraft make & model text fields
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).join(Aircraft).filter(Aircraft.aircraft_make == user_input_split[0] and
                                                                   Aircraft.aircraft_model == user_input_split[1]).all()
    elif input_type == "Event Date & Event Location":  # Input is entered as combo; event date & location text fields
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).filter(Incidents.event_date == user_input_split[0] and
                                                    Incidents.event_location == user_input_split[1]).all()
    elif input_type == "Event Date & Aircraft Registration":
        # Input is entered as combo; event date & aircraft reg num text fields
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).filter(Incidents.event_date == user_input_split[0] and
                                                    Incidents.aircraft_reg_number == user_input_split[1]).all()
    elif input_type == "Event Date & NTSB Number":  # Input is entered as combo; event date & NTSB number text fields
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).filter(Incidents.event_date == user_input_split[0] and
                                                    Incidents.event_ntsb_number == user_input_split[1]).all()
    elif input_type == "Event Date & Aircraft Make":
        # Input is entered as combo; event date & aircraft make text fields
        user_input_split = user_input.split(" ")
        sql_query = sql_query = session.query(Incidents).join(Aircraft).\
            filter(Incidents.event_date == user_input_split[0] and Aircraft.aircraft_make == user_input_split[1]).all()
    elif input_type == "Event Date & Aircraft Model":
        # Input is entered as combo; event date & aircraft model fields
        user_input_split = user_input.split(" ")
        sql_query = sql_query = session.query(Incidents).join(Aircraft). \
            filter(Incidents.event_date == user_input_split[0] and Aircraft.aircraft_model == user_input_split[1]).all()
    elif input_type == "Event Date & Event Severities":
        # Input is entered as combo; event date & casualties fields !!! NEED TO FIX THIS ONE !!!
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).filter(Incidents.event_date == user_input_split[0] and
                                                    Incidents.event_ntsb_number == user_input_split[1])
    elif input_type == "Aircraft Registration & NTSB Number":
        # Input is entered as combo; aircraft reg num & NTSB num fields
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).filter(Incidents.aircraft_reg_number == user_input_split[0] and
                                                    Incidents.event_ntsb_number == user_input_split[1])
    elif input_type == "Aircraft Registration & Event Location":
        # Input is entered as combo; aircraft reg num & event location fields
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).filter(Incidents.aircraft_reg_number == user_input_split[0] and
                                                    Incidents.event_location == user_input_split[1])
    elif input_type == "Aircraft Registration & Event Severity":
        # Input is entered as combo; event date & casualties fields !!! NEED TO FIX THIS ONE !!!
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).filter(Incidents.aircraft_reg_number == user_input_split[0] and
                                                    Incidents.event_severity == user_input_split[1])

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
