from flask import Flask,redirect,render_template,request

import joblib

model = joblib.load('model.pkl')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def predict_marks():
    if request.method == 'POST':
        hours = float(request.form['hours'])
        marks = str(model.predict([[hours]])[0][0])
    return render_template('index.html',m = marks)

if __name__=='__main__':
    app.run(debug = True)