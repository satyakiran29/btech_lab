from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index_app.html')

@app.route('/studentinsert')
def insert_record():
    return render_template('insert_app.html')

@app.route('/addstudent',methods=['GET','POST'])
def add_student():
    if request.method == 'POST':
        try:
            ueid = request.form['mailid']
            uname = request.form['username']
            upwd = request.form['pwd']
            with sqlite3.connect('studentdb.db') as con:
                cur = con.cursor()
                # Create table if it doesn't exist
                cur.execute('''CREATE TABLE IF NOT EXISTS STUDENT (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE,
                                password TEXT NOT NULL)''')
                cur.execute('INSERT INTO STUDENT(username, email, password) VALUES(?, ?, ?)', (uname, ueid, upwd))
                con.commit()
                msg = 'Record successfully Inserted'
        except:
            con.rollback()
            msg = 'Insert record Unsuccessful...TRY AGAIN!'
        finally:
            return render_template('result_app.html', msg=msg)
            con.close()

if __name__=='__main__':
    app.run(debug=True)