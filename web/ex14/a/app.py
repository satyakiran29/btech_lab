from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root', # Use your MySQL username
    'password': '', # Use your MySQL password (default is empty for XAMPP)
    'database': 'users_data' # Name of the database you created
}

# Route for home page
@app.route('/suce')
def home():
    return render_template('index.html')

# Route for registration page
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Insert data into MySQL database
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = 'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)'
            cursor.execute(query, (username, email, password))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('home'))
    return render_template('register.html')

if __name__ == '_main_':
    app.run(debug=True)