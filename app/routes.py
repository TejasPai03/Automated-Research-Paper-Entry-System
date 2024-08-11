from flask import render_template, request
from app import app
import mysql.connector
import pandas as pd
from config import Config


# Create a .config file and store details w.r.to the keys
db_config = {
    "host": Config.HOST,        # Set 'localhost' to run local instance
    "user": Config.USER,
    "password": Config.PASSWORD,
    "database": Config.DATABASE 
}


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    usn = request.form['usn'].lower()
    paperid = request.form['paperid']
    title = request.form['title']
    author = request.form['author']
    conference = request.form['conference']
    journal = request.form['journal']
    date = request.form['date']
    doi = request.form['doi']

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO research_papers (usn, paper_id, title, author, conference, journal, date, doi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (usn, paperid, title, author, conference, journal, date, doi)
        cursor.execute(query, data)
        query2 = "INSERT INTO writes VALUES(%s, %s)"
        data2 = (usn, paperid)
        cursor.execute(query2, data2) 
        conn.commit()
        cursor.close()
        conn.close()
        return "Paper submitted successfully!"
    except mysql.connector.Error as err:
        return f"Error: {err}"


@app.route('/usn-form', methods=['GET'])
def usn_form():
    return render_template('usn_form.html')


@app.route('/sql-data', methods=['POST'])
def sql_table():
    usn = request.form['usn']

    conn = mysql.connector.connect(**db_config)
    sql = "SELECT * FROM research_papers WHERE usn = %s;"
    mycursor = conn.cursor()
    mycursor.execute(sql, (usn,))
    myresult = mycursor.fetchall()

    df = pd.DataFrame(myresult, columns=['USN', 'Paper ID', 'Title', 'Author', 'Conference', 'Journal', 'Date', 'DOI'])
    df.to_html('templates/sql-data.html')
    return render_template('sql-data.html')


@app.route('/delete-data', methods=['GET'])
def delete_form():
    return render_template('delete_form.html')


@app.route('/submit-paper-id', methods=['POST'])
def delete_data():
    paper_id = request.form['paperid']
        
    conn = mysql.connector.connect(**db_config)
    mycursor = conn.cursor()
    
    sql = "DELETE FROM research_papers WHERE paper_id = %s;"
    mycursor.execute(sql, (paper_id,))
        
    conn.commit()
    mycursor.close()
    conn.close()

    return "Paper deleted successfully!"