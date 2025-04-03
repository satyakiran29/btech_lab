from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_PORT'] = 3306  # Change to 3306 if needed
app.config['MYSQL_DB'] = 'form2'

mysql = MySQL(app)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':
     
        if 'name' not in request.form or 'email' not in request.form or 'password' not in request.form:
            return "Error: Missing form fields!", 400

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']


        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return "Invalid email format!", 400

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO users (name, email, password) VALUES (%s, %s, %s)''', (name, email, password))
            mysql.connection.commit()
            cursor.close()

            return redirect(url_for('success'))

        except Exception as e:
            return f"Database Error: {str(e)}", 500  

@app.route('/success')
def success():
    return "User successfully registered!"

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
