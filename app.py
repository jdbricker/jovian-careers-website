#at commmand line run with 'python app.py' otherwise will run as module and name != main
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def hello_world():
    #return "return value"
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')