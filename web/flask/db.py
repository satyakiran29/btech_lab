import sqlite3
con=sqlite3.connect('studentdb.db')
print('Database Created Successfully')
cur=con.cursor()
cur.execute('CREATE TABLE student(username text, email text, password text)')
print('Table Created Successfully')
con.close()
