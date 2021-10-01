from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import InputRequired

class AddStudentForm(FlaskForm):
    name = StringField('Student name', validators=[InputRequired()])
    grade_id = SelectField('Grade', coerce=int)
    house_id = SelectField('House')
    english_mark = IntegerField('English', validators=[InputRequired()])
    science_mark = IntegerField('Science', validators=[InputRequired()])
    mathematics_mark = IntegerField('Mathematics', validators=[InputRequired()])
    does_homework = BooleanField('Does homework?')
    stays_on_task = BooleanField('Stays on task?')
    
    submit = SubmitField('Add student')
