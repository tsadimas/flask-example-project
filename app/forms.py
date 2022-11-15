from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class StudentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(2, 20)])
    city = StringField('city', validators=[DataRequired(), Length(3, 30)])
    country = StringField('country', validators=[DataRequired(), Length(3, 50)])
    submit = SubmitField()

class JobForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(5, 100)])
    submit = SubmitField()