from flask import Flask,render_template,request
import regex as re
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/out')
def submit():
    sentence = request.args.get('inputString')
    pattern = request.args.get('inputPattern')
    reg = re.compile(r'{}'.format(pattern))
    match = reg.search(sentence)
    return render_template('submit.html',sent=sentence,out=match.groups())
if __name__ == '__main__':
    app.run(debug=True)