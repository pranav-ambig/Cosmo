import mysql.connector

from flask import Flask, render_template, request
from flask_cors import CORS
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="spacedb",
  port=3307
)

app = Flask(__name__)
CORS(app)

cur = mydb.cursor(dictionary=True)

@app.route('/', methods=['GET'])
def home():
    return 'hello'

@app.route('/init')
def initial():
    cur.execute(f'SELECT * FROM Planet WHERE Planet.name = "Earth"')
    return cur.fetchall()

@app.route('/fetch', methods=['GET', 'POST'])
def fetchFromDB():

    data = request.json
    rel = data['rel']
    relid = data['relid']

    cur.execute(f'SELECT * FROM {rel} WHERE {rel}.{rel}ID = {relid}')
    return cur.fetchall()

@app.route('/planets')
def getPlanets():
    cur.execute('SELECT * FROM Planet')
    return cur.fetchall()

@app.route('/stars')
def getStars():
    cur.execute('SELECT * FROM Star')
    return cur.fetchall()

@app.route('/query', methods=['GET', 'POST'])
def Query():

    data = request.json
    try:
        cur.execute(data['query'])
        return cur.fetchall()
    except Exception as e:
        print(e)
        return 'Error'


if __name__ == "__main__":
    app.run(debug=True)
