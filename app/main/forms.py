#form imports
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, PasswordField
from wtforms.validators import DataRequired, NumberRange

slot_options = [(x,x) for x in "ABCDEFGPQRS"]
branches = ["AI","CS","CE","CH","EE","EP","ES","ME","MA","MS","ID","LA"]
branch_options = [(x,x) for x in branches]

class CourseForm(FlaskForm):
    name = StringField("Course Name",validators=[DataRequired()])
    courseType = SelectField(u'Department',choices = branch_options,validators=[DataRequired()])
    courseId = IntegerField(validators = [NumberRange(1000,9999),DataRequired()])
    link = StringField("Link",validators =[DataRequired()])
    slot = SelectField(u'Slot',choices = slot_options,validators=[DataRequired()])

class RemoverForm(FlaskForm):
    courseType = SelectField(u'Department',choices = branch_options,validators=[DataRequired()])
    courseId = IntegerField(validators = [NumberRange(1000,9999),DataRequired()])
    slot = SelectField(u'Slot',choices = slot_options,validators=[DataRequired()])
    password = PasswordField()

class PreferenceForm(FlaskForm):
    default_id = IntegerField(validators=[DataRequired()])
