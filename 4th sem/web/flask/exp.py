from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""  # Placeholder for success message

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        with sqlite3.connect("siva.db") as conn:
            conn.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()

        message = "Form submitted successfully!"  # Set success message

    return render_template("rev.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
