from flask import Flask, render_template
import sqlite3
from sqlite3 import Error
DATABASE = "C:/Users/22452/PycharmProjects/flaskProject/identifier.sqlite"

app = Flask(__name__)


def create_connection(db_file):
    """
    Create a connection with the database
    parameter: name of the database file
    returns: a connection to the file
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/')
def homework_list():
    con = create_connection(DATABASE)
    query = "SELECT Student_ID, First_Name, Last_Name, Email, Phone_Number FROM student"
    cur = con.cursor()
    cur.execute(query)
    student_list = cur.fetchall()
    query = "SELECT Student_ID, Subject, Title, Date FROM work"
    cur = con.cursor()
    cur.execute(query)
    work_list = cur.fetchall()
    con.close()
    return render_template('Homework_Page.html', student=student_list, work=work_list)


app.run(host='0.0.0.0', debug=True)
