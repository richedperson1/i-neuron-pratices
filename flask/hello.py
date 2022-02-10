from pydoc import render_doc
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world(name):
    return "Rutvik Jaiswal Got 12lpa package for data scientist "

@app.route("/even/<int:num>")
def odd_even(num):
    if num&1==0:
        return "<h1 style = 'color:brown'>Number is <b> Even </b></h1>"
    return "Number is <b> Odd </b>"

if __name__=='__main__':
    app.run(port=5001,host='0.0.0.0',debug = True)