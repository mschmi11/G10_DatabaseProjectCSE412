import os
import string
import psycopg2
import json
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, and_, select
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, Session

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
    c_list1 = list()
    c_list2 = list()
    c_list3 = list()
    c_list4 = list()
    c_list5 = list()
    c_list6 = list()
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
    cs1 = set()
    cs2 = set()
    cs3 = set()
    cs4 = set()
    cs5 = set()
    cs6 = set()
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
                    else:
                        incident_result_set = is1.intersection(is2)
                        incident_result_set = incident_result_set.intersection(is3)
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
    if casualties_id or casualties_age or casualties_sex or casualties_dob or casualties_first_name or casualties_last_name:
        casualties_queried = True
        if casualties_id:
            c_list1 = session.query(Casualties.event_ntsb_number).filter(Casualties.casualty_id == casualties_id).all()
            cs1 = set(c_list1)
        if casualties_age:
            c_list2 = session.query(Casualties.event_ntsb_number).filter(Casualties.age == casualties_age).all()
            cs2 = set(c_list2)
        if casualties_sex:
            c_list3 = session.query(Casualties.event_ntsb_number).filter(Casualties.sex == casualties_sex).all()
            cs3 = set(c_list3)
        if casualties_dob:
            c_list4 = session.query(Casualties.event_ntsb_number).filter(Casualties.dob == casualties_dob).all()
            cs4 = set(c_list4)
        if casualties_first_name:
            c_list5 = session.query(Casualties.event_ntsb_number).filter(Casualties.first_name == casualties_first_name).all()
            cs5 = set(c_list5)
        if casualties_last_name:
            c_list6 = session.query(Casualties.event_ntsb_number).filter(Casualties.last_name == casualties_last_name).all()
            cs6 = set(c_list6)

        if c_list1:
            if c_list2:
                if c_list3:
                    if c_list4:
                        if c_list5:
                            if c_list6:
                                casualty_result_set = cs1.intersection(cs2)
                                casualty_result_set = casualty_result_set.intersection(cs3)
                                casualty_result_set = casualty_result_set.intersection(cs4)
                                casualty_result_set = casualty_result_set.intersection(cs5)
                                casualty_result_set = casualty_result_set.intersection(cs6)
                            else:
                                casualty_result_set = cs1.intersection(cs2)
                                casualty_result_set = casualty_result_set.intersection(cs3)
                                casualty_result_set = casualty_result_set.intersection(cs4)
                                casualty_result_set = casualty_result_set.intersection(cs5)
                        elif c_list6:
                            casualty_result_set = cs1.intersection(cs2)
                            casualty_result_set = casualty_result_set.intersection(cs3)
                            casualty_result_set = casualty_result_set.intersection(cs4)
                            casualty_result_set = casualty_result_set.intersection(cs6)
                        else:
                            casualty_result_set = cs1.intersection(cs2)
                            casualty_result_set = casualty_result_set.intersection(cs3)
                            casualty_result_set = casualty_result_set.intersection(cs4)
                    elif c_list5:
                        if c_list6:
                            casualty_result_set = cs1.intersection(cs2)
                            casualty_result_set = casualty_result_set.intersection(cs3)
                            casualty_result_set = casualty_result_set.intersection(cs5)
                            casualty_result_set = casualty_result_set.intersection(cs6)
                        else:
                            casualty_result_set = cs1.intersection(cs2)
                            casualty_result_set = casualty_result_set.intersection(cs3)
                            casualty_result_set = casualty_result_set.intersection(cs5)
                    elif c_list6:
                        casualty_result_set = cs1.intersection(cs2)
                        casualty_result_set = casualty_result_set.intersection(cs3)
                        casualty_result_set = casualty_result_set.intersection(cs6)
                    else:
                        casualty_result_set = cs1.intersection(cs2)
                        casualty_result_set = casualty_result_set.intersection(cs3)
            elif c_list3:
                if c_list4:
                    if c_list5:
                        if c_list6:
                            casualty_result_set = cs1.intersection(cs3)
                            casualty_result_set = casualty_result_set.intersection(cs4)
                            casualty_result_set = casualty_result_set.intersection(cs5)
                            casualty_result_set = casualty_result_set.intersection(cs6)
                        else:
                            casualty_result_set = cs1.intersection(cs3)
                            casualty_result_set = casualty_result_set.intersection(cs4)
                            casualty_result_set = casualty_result_set.intersection(cs5)
                    elif c_list6:
                        casualty_result_set = cs1.intersection(cs3)
                        casualty_result_set = casualty_result_set.intersection(cs4)
                        casualty_result_set = casualty_result_set.intersection(cs6)
                    else:
                        casualty_result_set = cs1.intersection(cs3)
                        casualty_result_set = casualty_result_set.intersection(cs4)
                elif c_list5:
                    if c_list6:
                        casualty_result_set = cs1.intersection(cs3)
                        casualty_result_set = casualty_result_set.intersection(cs5)
                        casualty_result_set = casualty_result_set.intersection(cs6)
                    else:
                        casualty_result_set = cs1.intersection(cs3)
                        casualty_result_set = casualty_result_set.intersection(cs5)
                elif c_list6:
                    casualty_result_set = cs1.intersection(cs3)
                    casualty_result_set = casualty_result_set.intersection(cs6)
                else:
                    casualty_result_set = cs1.intersection(cs3)
            elif c_list4:
                if c_list5:
                    if c_list6:
                        casualty_result_set = cs1.intersection(cs4)
                        casualty_result_set = casualty_result_set.intersection(cs5)
                        casualty_result_set = casualty_result_set.intersection(cs6)
                    else:
                        casualty_result_set = cs1.intersection(cs4)
                        casualty_result_set = casualty_result_set.intersection(cs5)
                elif c_list6:
                    casualty_result_set = cs1.intersection(cs4)
                    casualty_result_set = casualty_result_set.intersection(cs6)
                else:
                    casualty_result_set = cs1.intersection(cs4)
            elif c_list5:
                if c_list6:
                    casualty_result_set = cs1.intersection(cs5)
                    casualty_result_set = casualty_result_set.intersection(cs6)
                else:
                    casualty_result_set = cs1.intersection(cs5)
            else:
                casualty_result_set = cs1
        elif c_list2:
            if c_list3:
                if c_list4:
                    if c_list5:
                        if c_list6:
                            casualty_result_set = cs2.intersection(cs3)
                            casualty_result_set = casualty_result_set.intersection(cs4)
                            casualty_result_set = casualty_result_set.intersection(cs5)
                            casualty_result_set = casualty_result_set.intersection(cs6)
                        else:
                            casualty_result_set = cs2.intersection(cs3)
                            casualty_result_set = casualty_result_set.intersection(cs4)
                            casualty_result_set = casualty_result_set.intersection(cs5)
                    elif c_list6:
                        casualty_result_set = cs2.intersection(cs3)
                        casualty_result_set = casualty_result_set.intersection(cs4)
                        casualty_result_set = casualty_result_set.intersection(cs6)
                    else:
                        casualty_result_set = cs2.intersection(cs3)
                        casualty_result_set = casualty_result_set.intersection(cs4)
                elif c_list5:
                    if c_list6:
                        casualty_result_set = cs2.intersection(cs3)
                        casualty_result_set = casualty_result_set.intersection(cs5)
                        casualty_result_set = casualty_result_set.intersection(cs6)
                    else:
                        casualty_result_set = cs2.intersection(cs3)
                        casualty_result_set = casualty_result_set.intersection(cs5)
                elif c_list6:
                    casualty_result_set = cs2.intersection(cs3)
                    casualty_result_set = casualty_result_set.intersection(cs6)
                else:
                    casualty_result_set = cs2.intersection(cs3)
            elif c_list4:
                    if c_list5:
                        if c_list6:
                            casualty_result_set = cs2.intersection(cs4)
                            casualty_result_set = casualty_result_set.intersection(cs5)
                            casualty_result_set = casualty_result_set.intersection(cs6)
                        else:
                            casualty_result_set = cs2.intersection(cs4)
                            casualty_result_set = casualty_result_set.intersection(cs5)
                    elif c_list6:
                        casualty_result_set = cs2.intersection(cs4)
                        casualty_result_set = casualty_result_set.intersection(cs6)
                    else:
                        casualty_result_set = cs2.intersection(cs4)
            elif c_list5:
                if c_list6:
                    casualty_result_set = cs2.intersection(cs5)
                    casualty_result_set = casualty_result_set.intersection(cs6)
                else:
                    casualty_result_set = cs2.intersection(cs5)
            else:
                casualty_result_set = cs2
        elif c_list3:
            if c_list4:
                if c_list5:
                    if c_list6:
                        casualty_result_set = cs3.intersection(cs4)
                        casualty_result_set = casualty_result_set.intersection(cs5)
                        casualty_result_set = casualty_result_set.intersection(cs6)
                    else:
                        casualty_result_set = cs3.intersection(cs4)
                        casualty_result_set = casualty_result_set.intersection(cs5)
                elif c_list6:
                    casualty_result_set = cs3.intersection(cs4)
                    casualty_result_set = casualty_result_set.intersection(cs6)
                else:
                    casualty_result_set = cs3.intersection(cs4)
            elif c_list5:
                if c_list6:
                    casualty_result_set = cs3.intersection(cs5)
                    casualty_result_set = casualty_result_set.intersection(cs6)
                else:
                    casualty_result_set = cs3.intersection(cs5)
            elif c_list6:
                casualty_result_set = cs3.intersection(cs6)
            else:
                casualty_result_set = cs3
        elif c_list4:
            if c_list5:
                if c_list6:
                    casualty_result_set = cs4.intersection(cs5)
                    casualty_result_set = casualty_result_set.intersection(cs6)
                else:
                    casualty_result_set = cs4.intersection(cs5)
            elif c_list6:
                casualty_result_set = cs4.intersection(cs6)
            else:
                casualty_result_set = cs4
        elif c_list5:
            if c_list6:
                casualty_result_set = cs5.intersection(cs6)
            else:
                casualty_result_set = cs5
        elif c_list6:
            casualty_result_set = cs6
        else:
            casualty_result_set = cs1

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

    return render_template("index.html", result_user_entry_to_sql=result_set)


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
    result_countaircraft = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", result_countaircraft=result_countaircraft)


# queries
# Select aircraft with an incident on user date
@app.route("/aircraftIncidentOnDate", methods=['POST'])
def aircraftIncidentOnDate():
    incident_date = request.form["incident_date"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM Aircraft, Incidents WHERE Aircraft.aircraft_reg_number=Incidents.aircraft_reg_number AND Incidents.event_date=\'' + incident_date + '\';')
    result_aircraftIncidentOnDate = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", result_aircraftIncidentOnDate=result_aircraftIncidentOnDate)


# Select all incidents by aircraft model
@app.route("/incidentsByModel", methods=['POST'])
def incidentsByModel():
    aircraft_model2 = request.form["aircraft_model2"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM Aircraft, Incidents WHERE Aircraft.aircraft_reg_number=Incidents.aircraft_reg_number AND Aircraft.aircraft_model=\'' + aircraft_model2 + '\';')
    result_incidentsByModel = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", result_incidentsByModel=result_incidentsByModel)


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
    result_insertAircraft = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", result_insertAircraft=result_insertAircraft)
    

# Update an aircraft
@app.route("/updateAircraft", methods=['POST'])
def updateAircraft():
    aircraft_model_update = request.form["aircraft_model_update"]
    aircraft_reg_num_update = request.form["aircraft_reg_num_update"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE AIRCRAFT SET aircraft_model=\'' + aircraft_model_update + '\' WHERE aircraft_reg_number=\'' + aircraft_reg_num_update + '\';SELECT * FROM Aircraft WHERE aircraft_reg_number=\'' + aircraft_reg_num_update + '\';')
    result_updateAircraft = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", result_updateAircraft=result_updateAircraft)
     

# Update an aircraft
@app.route("/deleteCasualty", methods=['POST'])
def deleteCasualty():
    casualty_id_delete = request.form["casualty_id_delete"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'DELETE FROM Casualties WHERE casualty_id=\'' + casualty_id_delete + '\';')
    #result_updateAircraft = cur.fetchall()
    result_updateAircraft = casualty_id_delete + "deleted."
    cur.close()
    conn.close()
    return render_template("index.html", result_deleteCasualty=casualty_id_delete+" deleted.")
    

# Get data for map Function
@app.route("/map_function", methods=['POST'])
def map_function():
    conn = get_db_connection()
    cur = conn.cursor()
    
    states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut",  "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
    
    result_map_function = []
    for i in (states):
    	cur.execute('SELECT * FROM Incidents WHERE event_state=\'' + i + '\';')
    	state = cur.fetchall()
    	print(state)
    	if not (state is None):
    		result_map_function.append(state)
    
    print(result_map_function)
    cur.close()
    conn.close()
    return json.dumps(result_map_function)
    
    
    
    
    
    
    
    
    
    
