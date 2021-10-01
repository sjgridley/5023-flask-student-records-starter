from flask import render_template, redirect, url_for

from app import app, db
from app.models import Student, Grade, House
from app.forms import AddStudentForm

def get_grade_choices():
    ''' A helper function that returns a list of
        tuples with grade ids and names from the grades table.
        This is used to populate the choices in the Grade dropdown.
        This could be written more succinctly with a list comprehension.
    '''
    grade_choices = []
    for grade in Grade.query.all():
        choice = (grade.id, grade.name)
        grade_choices.append(choice)
    return grade_choices

def get_house_choices():
    ''' A helper function that returns a list of
        tuples with house ids and names from the houses table.
        This is used to populate the choices in the House dropdown.
        This could be written more succinctly with a list comprehension.
    '''
    house_choices = []
    for house in House.query.all():
        choice = (house.id, house.name)
        house_choices.append(choice)
    return house_choices


@app.route('/')
def index():
    # Load the students from the database file for the table
    students = Student.query.all()
    # Return the index view with the list of students for display
    return render_template('index.html', students = students)

@app.route('/add_student', methods = ['GET', 'POST'])
def add_student():
    form = AddStudentForm()
    form.grade_id.choices = get_grade_choices()
    form.house_id.choices = get_house_choices()
    
    # Check if the form has been submitted (is a POST request) and form inputs are valid
    if form.validate_on_submit():
        # Get data from the form and put in a Student object
        student = Student()
        form.populate_obj(obj=student)
        db.session.add(student)
        db.session.commit()
        
        # Returns the view with a message that the student has been added
        return redirect(url_for('index'))

    # When there is a GET request, the view with the form is returned
    return render_template('add_student.html', form = form)