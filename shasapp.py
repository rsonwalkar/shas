__author__ = 'rohit.sonwalkar'


import pprint
import os
import json
from flask import Flask, request, jsonify
import pymysql

# setting the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

# @app.route("/", methods=['GET'])
# def login():
#     return app.send_static_file('login.html')

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return app.send_static_file('login.html')
    # elif request.method == 'POST':
    #     return jsonify(request.get_json())
        # conn = pymysql.connect(host='localhost', port=3306, db='test')
        # cursor = conn.cursor()
        # cursor.execute('select * from persons')
        # for rows in cursor.fetchall():
        #     return str(rows)

@app.route("/authenticate", methods=['POST'])
def authenticate():
    username = request.get_json()['username']
    password = request.get_json()['password']
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='test')
    cursor = conn.cursor()
    cursor.execute('select fname, lname from login where username="' + username + '" and password="' + password + '"')
    rows = cursor.fetchall()
    response = {}
    if len(rows) > 0:
        response['fname'] = rows[0][0]
        response['lname'] = rows[0][1]
        return jsonify(**response)
    else:
        return jsonify({'error': 'Could not authenticate'})

@app.route("/adduser", methods=['POST'])
def adduser():
    fname = request.get_json()['fname']
    lname = request.get_json()['lname']
    username = request.get_json()['username']
    password = request.get_json()['password']
    conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='test')
    cursor = conn.cursor()
    cursor.execute('insert into login values ("' + fname + '","' + lname + '","' + username + '","' + password + '")')
    # The commit will insert the new entry into the database
    conn.commit()
    return jsonify({'success': 'row inserted'})

@app.route("/home", methods=['GET'])
def home():
    return app.send_static_file('index.html')

    # for rows in cursor.fetchall():
    #     return str(rows)
    # # print(request.get_json()['username'])
    # # return 'Hello'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int("3333"))
