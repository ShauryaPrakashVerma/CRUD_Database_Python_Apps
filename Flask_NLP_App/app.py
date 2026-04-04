from flask import Flask, render_template, request, redirect, session
from db import Database
import api

app = Flask(__name__)
app.secret_key = 'ek mota haathi'
dbo = Database()

# basically creating a url
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def signup():
    return render_template('register.html')

@app.route('/perform_registration', methods = ['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.insert(name, email, password)
    if response ==1:
        return render_template('login.html', message = "Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html', message = "Email already exists..")
    
    return name + " " + email + " " + password

@app.route('/perform_login', methods = ['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search(email, password)
    if response == 1:
        session.get( 'logged_in', 0) == 1
        return redirect('/profile')
    else:
        return render_template('login.html', message = "Wrong Email / Password. Please try again.")

@app.route('/profile')
def profile():
    if session.get('logged_in', 0) == 1:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session.get('logged_in', 0) == 1:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    if session.get('logged_in', 0) == 1:
        text = request.form.get('user_input')
        response = api.ner(text)
        print(response)
        return 'something'
    else:
        return redirect('/')



@app.route('/sentiment_analysis')
def sentiment_analysis():
    return render_template('sentiment_analysis.html')

@app.route('/abuse_detection')
def abuse_detection():
    return render_template('abuse_detection.html')

@app.route('/facial_recognition')
def facial_recognition():
    return render_template('facial_recognition.html')



app.run(debug = True)  # without debug =True any changes made are not reflected until the program is executed again.
                    #  with debug = True any changes made are directly reflected on th eweb page