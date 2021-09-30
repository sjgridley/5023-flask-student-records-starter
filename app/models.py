from app import db

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    students = db.relationship('Student', backref='grade')

# TODO: Add a class for the database model for the House table

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=False)
    # TODO: Add a house_id column, a foreign key to the House table, once the House model has been defined
    english_mark = db.Column(db.Integer)
    science_mark = db.Column(db.Integer)
    # TODO: Add a column for a student's mathematics mark
    does_homework = db.Column(db.Boolean)
    # TODO: Add a column for a student's stay_on_task behaviour
