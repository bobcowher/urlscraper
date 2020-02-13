from flask import Flask, render_template
from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from flask import Flask,request
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from scan_lib import getUrl, getTextPurpose
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class ScanForm(FlaskForm):
    """Contact form."""
    url = StringField('url', [
        DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def home():
    return("Hello, I'm the url scraper. Go to /scan for something useful")
 
@app.route('/scan', methods=('GET', 'POST'))
def scan():
    form = ScanForm()
    return render_template("scan.html", form=form)

@app.route('/results', methods=('GET', 'POST'))
def results():
    freq = getTextPurpose(getUrl(request.form['url']))
    
    for key,val in freq.items():
        return((str(key) + ':' + str(val)))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')