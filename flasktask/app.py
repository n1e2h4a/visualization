from io import BytesIO
from flask import Flask, render_template, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np

import jinja2
import matplotlib.pyplot as plt
import pandas as pd
import jinja2
plt.style.use('ggplot')

from flask import Flask, render_template, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

plt.style.use('ggplot')

app = Flask(__name__)

my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('/home/niharika/PycharmProjects/visualize/venv/my')
])



app.jinja_loader = my_loader


@app.route('/data')
def pie_visu():
    fig, ax = plt.subplots()
    df=pd.read_csv('data.csv')
    df1=df['Gender'].value_counts()
    df = pd.read_csv('data.csv')
    df1 = df['Gender'].value_counts()
    label = ["male", "Female"]
    print(df1)
    colors = ["#1f77b5", "#ff7f0f"]
    plt.pie(df1, colors=colors, labels=label, shadow=True, autopct='%1.2f%%')
    canvas=FigureCanvas(fig)
    img=BytesIO()
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


# @app.route('/data1')
# def bar():
#     df = pd.read_csv('D:\\FLASK_NEW\\EXample\\Data.csv')



#
@app.route('/')
def index():
    return render_template('index.html')



if __name__ =='__main__':

    app.run(debug=True)






