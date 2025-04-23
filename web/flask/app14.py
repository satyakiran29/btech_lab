from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    error = ''
    success = ''
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        
        if not name:
            error = 'Name is required'
        elif '@' not in email or '.' not in email:
            error = 'Valid email is required'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters'
        else:
            success = 'Registration successful!'
    
    return render_template('login.html', error=error, success=success)

if __name__ == '__main__':
    app.run(debug=True)