__author__ = 'rohit.sonwalkar'


import pprint
import os
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
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return username
        # conn = pymysql.connect(host='localhost', port=3306, db='test')
        # cursor = conn.cursor()
        # cursor.execute('select * from persons')
        # for rows in cursor.fetchall():
        #     return str(rows)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int("3333"))
