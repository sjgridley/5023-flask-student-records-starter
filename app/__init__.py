from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Turns this setting off, helps with performance
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'example-secret' #Used for demonstration, DO NOT use in production

db = SQLAlchemy(app)

from app import routes
from app.models import Student, Grade

@app.cli.command('init-db')
def create_db():
    # Recreate database for defined models
    db.drop_all()
    db.create_all()

    year4 = Grade(name='Year 4')
    db.session.add(year4)

    year5 = Grade(name='Year 5')
    db.session.add(year5)

    year6 = Grade(name='Year 6')
    db.session.add(year6)

    # TODO: Add code that creates new House records, once that model has been defined

    # Creates two example students, we do not need to add these to the sessions explicitly
    # Flask-SQLAlchemy works out that they need to be added, as they are linked to the grade records above.
    jack = Student (
        name = 'Jack',
        grade = year6,
        # TODO: Add the house_id field once it has been defined in the Student model
        english_mark = 90,
        science_mark = 90,
        # TODO: Add a value for the mathematics_mark field once it has been defined in the Student model
        does_homework = True,
        # TODO: Add a value for the stays_on_task field once it has been defined in the Student model
    )

    dom = Student (
        name = 'Dom',
        grade = year5,
        # TODO: Add the house_id field once it has been defined in the model
        english_mark = 90,
        science_mark = 100,
        # TODO: Add a value for the mathematics_mark field once it has been defined in the Student model
        does_homework = True,
        # TODO: Add a value for the stays_on_task field once it has been defined in the Student model
    )

    db.session.commit()


