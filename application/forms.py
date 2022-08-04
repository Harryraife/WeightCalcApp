from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from datetime import date

class NewUser(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    username = StringField("Please create a username", validators=[DataRequired()])
    submit = SubmitField("Submit")

class NewLift(FlaskForm):
    date = DateField("Day the lift was comleted")
    weight = IntegerField("Weight lifted in kg", validators=[DataRequired()])
    reps = IntegerField("Reps completed", validators=[DataRequired(),NumberRange(min=1, max=12)])
    lift = SelectField("Movement", choices=[
        ("squat","Squat"),
        ("bench","Bench"),
        ("deadlift","Deadlift")
    ], validators=[DataRequired()])
    user = SelectField("please input your username", choices = [])
    submit = SubmitField("Submit")
