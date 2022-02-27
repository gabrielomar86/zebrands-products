from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, DataRequired

class LoginForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=50)])
    submit_field = SubmitField('Login')
