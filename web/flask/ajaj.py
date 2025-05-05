from flask import Flask, redirect, url_for 
app = Flask(__name__) 
@app.route('/') 
def home(): 
   return "Welcome to GMRIT page!" 
@app.route('/a') 
def about(): 
   return "This is the about page." 
@app.route('/profile/<username>') 
def profile(username):  
   return "Welcome to the profile page of {username}." 
@app.route('/login') 
def login(): 
# Redirect to the home route 
   return redirect(url_for('about')) 
if __name__ == '__main__': 
   app.run(debug=True) 