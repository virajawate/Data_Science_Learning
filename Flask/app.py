# Simple Application
from flask import Flask, render_template, request, redirect, url_for

# Create Flask App

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello, Flask World!<h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to Flask Tutorial...."

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed the course with a score of "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return f"With score : {score} how can you pass?"

@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'GET':
        return render_template("calcualte.html")
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        language= float(request.form['language'])

        marks_avg = (maths + science + history + language) / 3
        result = ""
        if marks_avg >= 50:
            result = "Success"
        else:
            result = "Fail"
        
        return render_template('resukt.html', results = marks_avg)
    
#Assign a try loop

if __name__ == '__main__':
    app.run(debug=True)