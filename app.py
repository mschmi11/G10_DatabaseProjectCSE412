import os
import psycopg2
from flask import Flask, render_template
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='aircraft_db',
                            user='admin',
                            password='admin')
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM Aircraft;')
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
