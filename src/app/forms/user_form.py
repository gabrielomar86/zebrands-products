from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, DataRequired

class UserForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired(), Length(min=4, max=80)])
    email = StringField('Email', validators=[Email(), DataRequired(), Length(min=8, max=120)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=50)])
    submit_field = SubmitField('Save changes')
