#at commmand line run with 'python app.py' otherwise will run as module and name != main
from flask import Flask, render_template, Response
import pandas as pd
import numpy as np
from io import BytesIO

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def hello_world():
    #return "return value"
    return render_template('home.html',test='test string', l='1 2 3 4 5'.split())

@app.route('/graph.png')
def do_graph_png():
    pd.options.plotting.backend='plotly'

    df = (
        pd.DataFrame({
            'x':np.random.randn(100),
            'y':np.random.randn(100),
            'color':np.random.choice('red yellow green blue'.split(),100)
            }
        )
    )

    fig = df.plot(
        kind='scatter',
        x='x',
        y='y',
        c='color',
    )

    bytes_png = BytesIO()
    bytes_png.write(fig.to_image('png'))

    return Response(bytes_png.getvalue(), mimetype='image/png')

@app.route('/graph.html')
def do_graph_html():
    pd.options.plotting.backend='plotly'

    df = (
        pd.DataFrame({
            'x':np.random.randn(100),
            'y':np.random.randn(100),
            'color':np.random.choice('red yellow green blue'.split(),100)
            }
        )
    )

    fig = df.plot(
        kind='scatter',
        x='x',
        y='y',
        c='color',
    )

    #return(fig.to_html())
    return Response(fig.to_html(), mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')