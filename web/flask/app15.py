import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("studentdb.db")
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn

@app.route('/')
def fetch_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, email, password FROM student")  # Query user data
    data = cursor.fetchall()
    conn.close()
    return render_template('data.html', records=data)

if __name__ == '__main__':
    app.run(debug=True)