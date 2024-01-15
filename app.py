from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, template_folder='templates')
# MySQL configuration
db_config = {
    "host": "localhost", 
    "user": "root",
    "password": "",     # Enter your mysql server password
    "database": "phd_papers" # Change the Schema name if needed
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

    # Store the form data in the MySQL database
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



# Route to display the USN form
@app.route('/delete-data', methods=['GET'])
def delete_form():
    return render_template('delete_form.html')

# Route to handle data deletion
@app.route('/submit-paper-id', methods=['POST'])
def delete_data():
    # Get the Paper ID from the request
    paper_id = request.form['paperid']
        
    # Connect to the MySQL database
    conn = mysql.connector.connect(**db_config)
    mycursor = conn.cursor()
    
    # Execute the DELETE query
    sql = "DELETE FROM research_papers WHERE paper_id = %s;"
    mycursor.execute(sql, (paper_id,))
        
    # Commit the changes and close the connection
    conn.commit()
    mycursor.close()
    conn.close()
        
    # Return a success message (you can customize the message as needed)
    return "Paper deleted successfully!"

if __name__ == '__main__':
    app.run(port=5500, debug=True)
