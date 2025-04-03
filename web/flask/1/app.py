from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import re

app = Flask(__name__)


DATABASE = "form2.db"

def create_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

create_table()

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate email format
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return "Invalid email format!", 400

        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
                conn.commit()
            return redirect(url_for('success'))

        except sqlite3.IntegrityError:
            return "Error: Email already exists!", 400

@app.route('/success')
def success():
    return "User successfully registered!"

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
