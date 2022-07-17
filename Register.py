import re
from winreg import QueryInfoKey
from flask import Flask, request, render_template, redirect
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

myapp = Flask(__name__)


@myapp.route("/")
def homepage():
    return render_template("Register.html")


@myapp.route("/", methods=["POST"])
def checklogin():
    UN = request.form['Email']
    PW = request.form['Password']

    sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")
    cursor = sqlconnection.cursor()

    query1 = "SELECT * FROM Users WHERE Username='{un}' AND Password='{pw}'".format(
        un=UN, pw=PW)
    cursor.execute(query1)
    results = cursor.fetchall()
    if len(results) == 1:
        return render_template("index.html")
    else:
        return redirect("/register")


@myapp.route("/register", methods=["GET", "POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form['Email']
        dPW = request.form['Password']
        sqlconnection = sqlite3.Connection(currentlocation + "\Login.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES('{e}','{p}')".format(e=dUN, p=dPW)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("Register.html")


if __name__ == "__main__":
    myapp.run()
