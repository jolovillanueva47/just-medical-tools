from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

class BMIForm(FlaskForm):
    weight = DecimalField("Weight in kilograms:", validators=[DataRequired()])
    height = DecimalField("Height in meters:", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bmi", methods=['GET','POST'])
def bmi():
    weight=None
    height=None
    bmi=None
    formatted_bmi=None
    form=BMIForm()
    if form.validate_on_submit():
        print("form validated")
        weight=form.weight.data
        height=form.height.data
        bmi=weight/height**2
        formatted_bmi="{:.2f}".format(bmi)
    return render_template('bmi.html', bmi=formatted_bmi, form=form)


if __name__ == "__main__":
    app.run()