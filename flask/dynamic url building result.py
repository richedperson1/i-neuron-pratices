
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return "This is final result page made by Rutvik S Jaiswal ...! "

@app.route("/fail/<int:values>")
def fail(values):
    return "Sorry, Better luck next times 🤔🤔"+str(f" And your score is {values} ")


@app.route("/pass/<int:values>")
def passs(values):
    return "Yess you did it 😍😘😍😎,Exam is clear "+str(f" And your score is {values} ")

@app.route("/result/<int:mark>")
def result(mark):
    final_out = ''
    if mark<40:
        final_out =  'fail'
    else:
        final_out = "passs"

    return redirect(url_for(final_out,values = mark))

if __name__=='__main__':
    app.run(debug = True,host = '0.0.0.0')