import os
import string
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, Session
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, select

app = Flask(__name__)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:admin@localhost/aircraft_db"

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Incidents = Base.classes.incidents
Aircraft = Base.classes.aircraft
Casualties = Base.classes.casualties

session = Session(db.engine)


# establishes connection to DB
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='aircraft_db',
                            user='admin',
                            password='admin')
    return conn


# takes in input_type: the data type of field entered (EX: Aircraft Registration Number) user input
# creates SQL query through SQLAlchemy


@app.route("/user_entry_to_sql", methods=['POST'])
def user_entry_to_sql():
    aircraft_reg_num = request.form["aircraft_reg_num"]
    aircraft_model = request.form["aircraft_model"]
    aircraft_make = request.form["aircraft_make"]
    aircraft_event_ntsb_num = request.form["aircraft_event_ntsb_num"]
    casualties_id = request.form["casualties_id"]
    casualties_first_name = request.form["casualties_first_name"]
    casualties_last_name = request.form["casualties_last_name"]
    casualties_dob = request.form["casualties_dob"]
    casualties_age = request.form["casualties_age"]
    casualties_sex = request.form["casualties_sex"]
    casualties_event_ntsb_num = request.form["casualties_event_ntsb_num"]
    incident_event_ntsb = request.form["incident_event_ntsb"]
    incident_event_severity = request.form["incident_event_severity"]
    incident_event_date = request.form["incident_event_date"]
    incident_event_location = request.form["incident_event_location"]
    incident_aircraft_reg_num = request.form["incident_aircraft_reg_num"]
    user_input: string
    a_list1 = list()
    a_list2 = list()
    a_list3 = list()
    i_list1 = list()
    i_list2 = list()
    i_list3 = list()
    i_list4 = list()
    incident_queried = False
    aircraft_queried = False
    casualties_queried = False
    result_set = set()
    as1 = set()
    as2 = set()
    as3 = set()
    is1 = set()
    is2 = set()
    is3 = set()
    is4 = set()
    aircraft_result_set = set()
    incident_result_set = set()
    casualty_result_set = set()

    if aircraft_model or aircraft_make or aircraft_reg_num:
        aircraft_queried = True
        if aircraft_model:
            a_list1 = session.query(Aircraft.event_ntsb_number).filter(Aircraft.aircraft_model == aircraft_model).all()
            as1 = set(a_list1)
        if aircraft_make:
            a_list2 = session.query(Aircraft.event_ntsb_number).filter(Aircraft.aircraft_make == aircraft_make).all()
            as2 = set(a_list2)
        if aircraft_reg_num:
            a_list3 = session.query(Aircraft.event_ntsb_number).filter(Aircraft.aircraft_reg_number ==
                                                                       aircraft_reg_num).all()
            as3 = set(a_list3)

        if a_list1:
            if a_list2:
                if a_list3:
                    aircraft_result_set = as1.intersection(as2)
                    aircraft_result_set = aircraft_result_set.intersection(as3)
                else:
                    aircraft_result_set = as1.intersection(as2)
            elif a_list3:
                aircraft_result_set = as1.intersection(as3)
            else:
                aircraft_result_set = as1
        elif a_list2:
            if a_list3:
                aircraft_result_set = as2.intersection(as3)
            else:
                aircraft_result_set = as2
        elif a_list3:
            aircraft_result_set = as3
    if incident_event_ntsb or incident_event_date or incident_event_location or incident_event_severity:
        incident_queried = True
        if incident_event_ntsb:
            i_list1 = session.query(Incidents.event_ntsb_number).filter(Incidents.event_ntsb_number == incident_event_ntsb).all()
            is1 = set(i_list1)
        if incident_event_date:
            i_list2 = session.query(Incidents.event_ntsb_number).filter(Incidents.event_date == incident_event_date).all()
            is2 = set(i_list2)
        if incident_event_location:
            i_list3 = session.query(Incidents.event_ntsb_number).filter(Incidents.event_location == incident_event_location).all()
            is3 = set(i_list3)
        if incident_event_severity:
            i_list4 = session.query(Incidents.event_ntsb_number).filter(Incidents.event_severity == incident_event_severity).all()
            is4 = set(i_list4)
        if i_list1:
            if i_list2:
                if i_list3:
                    if i_list4:
                        incident_result_set = is1.intersection(is2)
                        incident_result_set = incident_result_set.intersection(is3)
                        incident_result_set = incident_result_set.intersection(is4)
                elif i_list4:
                    incident_result_set = is1.intersection(is2)
                    incident_result_set = incident_result_set.intersection(is4)
                else:
                    incident_result_set = is1.intersection(is2)
            elif i_list3:
                if i_list4:
                    incident_result_set = is1.intersection(is3)
                    incident_result_set = incident_result_set.intersection(is4)
                else:
                    incident_result_set = is1.intersection(is3)
            elif i_list4:
                incident_result_set = is1.intersection(is4)
            else:
                incident_result_set = is1
        elif i_list2:
            if i_list3:
                if i_list4:
                    incident_result_set = is2.intersection(is3)
                    incident_result_set = incident_result_set.intersection(is4)
                else:
                    incident_result_set = is2.intersection(is3)
            elif i_list4:
                incident_result_set = is2.intersection(is4)
            else:
                incident_result_set = is2
        elif i_list3:
            if i_list4:
                incident_result_set = is3.intersection(is4)
            else:
                incident_result_set = is3
        elif i_list4:
            incident_result_set = is4

    if aircraft_queried:
        if incident_queried:
            if casualties_queried:
                result_set = aircraft_result_set.intersection(incident_result_set)
                result_set = result_set.intersection(casualty_result_set)
            else:
                result_set = aircraft_result_set.intersection(incident_result_set)
        elif casualties_queried:
            result_set = aircraft_result_set.intersection(casualty_result_set)
        else:
            result_set = aircraft_result_set
    elif incident_queried:
        if casualties_queried:
            result_set = incident_result_set.intersection(casualty_result_set)
        else:
            result_set = incident_result_set
    else:
        result_set = casualty_result_set

    return render_template("index.html", resultSearch=result_set)
'''
    incidents_ntsb_num_list = db.select([Incidents.event_ntsb_number])
    incidents_set = set(incidents_ntsb_num_list)
    result_set = result_set.intersection(incidents_set)
    '''


'''
    elif incident_event_ntsb or incident_event_severity or incident_event_date or incident_event_location
        if incident_event_ntsb:
            i_list1 = db.select([Incidents.columns.])
        if incident_event_severity:
        if incident_event_date:
        if incident_event_location:
        
    list_incidents
    list_casualties
    result_test = db.session.query(Aircraft).filter_by(aircraft_model='A234')
   


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
    elif input_type == "Event Location & Aircraft Model":
        # Input is entered as combo; event location & aircraft model fields
        user_input_split = user_input.split(" ")
        sql_query = sql_query = session.query(Incidents).join(Aircraft). \
            filter(Incidents.event_location == user_input_split[0] and
                   Aircraft.aircraft_model == user_input_split[1]).all()
    elif input_type == "Event Location & Aircraft Make":
        # Input is entered as combo; event location & aircraft model fields
        user_input_split = user_input.split(" ")
        sql_query = sql_query = session.query(Incidents).join(Aircraft). \
            filter(Incidents.event_location == user_input_split[0] and
                   Aircraft.aircraft_make == user_input_split[1]).all()
    elif input_type == "Event Location & NTSB Number":
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).filter(Incidents.event_location == user_input_split[0] and
                                                    Incidents.event_ntsb_number == user_input_split[1]).all()
    elif input_type == "Event Location & Event Severities":
        # Input is entered as combo; event date & casualties fields !!! NEED TO FIX THIS ONE !!!
        user_input_split = user_input.split(" ")
        sql_query = session.query(Incidents).filter(Incidents.event_location == user_input_split[0] and
                                                    Incidents.event_severity == user_input_split[1])
    index(sql_query)
'''


# this runs at the start of the program
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
    cur.execute(
        'SELECT DISTINCT Aircraft.aircraft_reg_number FROM Aircraft, Incidents WHERE Aircraft.aircraft_reg_number=Incidents.aircraft_reg_number AND Incidents.event_date=\'' + incident_date + '\';')
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
    cur.execute(
        'SELECT DISTINCT Incidents.event_ntsb_number FROM Aircraft, Incidents WHERE Aircraft.aircraft_reg_number=Incidents.aircraft_reg_number AND Aircraft.aircraft_model=\'' + aircraft_model2 + '\';')
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
    cur.execute(
        'INSERT INTO Aircraft VALUES (' + aircraft_reg_num_insert + ', NULL, \'' + aircraft_make_insert + '\', \'' + aircraft_model_insert + '\'); SELECT * FROM Aircraft WHERE aircraft_reg_number=\'' + aircraft_reg_num_insert + '\';')
    result_insert = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", result_insert=result_insert)
