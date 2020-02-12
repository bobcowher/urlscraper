from flask import Flask, render_template
from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
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
    getTextPurpose(getUrl("https://en.wikipedia.org/wiki/SpaceX"))

    return render_template('home.html',)
 
@app.route('/scan', methods=('GET', 'POST'))
def scan():
    form = ScanForm()
    if form.validate_on_submit():
        return render_template("home.html") #This really doesn't work for some reason.
    return render_template("scan.html", form=form)

@app.route('/results', methods=('GET', 'POST'))
def results():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')