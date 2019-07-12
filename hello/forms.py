from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,IntegerField
from wtforms.validators import DataRequired,Length,NumberRange

class HelloForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(1,20)])
    body=TextAreaField('Message',validators=[DataRequired(),Length(1,200)])
    age=IntegerField('age',validators=[NumberRange(min=1,max=100)])
    score=IntegerField('score',validators=[NumberRange(min=1,max=100)])
    submit=SubmitField()