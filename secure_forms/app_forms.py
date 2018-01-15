from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import Email, DataRequired, Length, NumberRange

class MyForm(FlaskForm):
    names = StringField("Names", validators=[DataRequired(message="Enter Name!"), Length(min=6)])
    email = StringField("Email", validators=[DataRequired(message="Enter Email!"), Email(message="Enter valid Email")])
    age = IntegerField("Age", validators=[DataRequired(message="Enter Age!"), NumberRange(min=1, max=100, message="Age range is between 1 and 100")])
    password = PasswordField("Password", validators=[DataRequired(message="Enter Password"), Length(min=6)])


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="Enter Email!"), Email(message="Enter valid Email")])
    password = PasswordField("Password", validators=[DataRequired(message="Enter Password")])