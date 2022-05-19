from flask import *
app = Flask(__name__, template_folder='statics', static_folder='staticsss')


@app.route("/", methods=['POST', 'GET'])
def home_page():
    if request.method == 'POST':
        a = request.form['song_1']
        f = open('open.txt', 'a+')
        f.write(str(a)+'\n')
        f.close()
        return redirect(url_for('suggest', usr=3))
    return render_template('home.html')


@app.route("/suggection_song<int:usr>")
def suggest(usr):
    if request.method == "GET":
        return "Completed basic part of program"


app.run(debug=True)
