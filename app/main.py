from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from .forms import StudentForm, JobForm
from flask_bootstrap import Bootstrap5
# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SECRET_KEY'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SECRET_KEY")



db = SQLAlchemy(app)

class Student(db.Model):
  id = db.Column('student_id', db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  city = db.Column(db.String(50))
  country = db.Column(db.String(200))
  jobs = db.relationship('Job', backref='student', lazy=True)


  def __init__(self, name, city, country):
    self.name = name
    self.city = city
    self.country = country


class Job(db.Model):
    id = db.Column('job_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)

    def __init__(self, name, stid):
      self.name = name
      self.student_id = stid




with app.app_context():
  db.create_all()

@app.route('/')
def show_all():
  return render_template('show_all.html', students = Student.query.all() )

@app.route('/student', methods = ['GET', 'POST'])
def newstudent():
  form = StudentForm()
  if request.method == 'POST':
    if form.validate_on_submit():
      student = Student(request.form['name'], request.form['city'], request.form['country'])
      db.session.add(student)
      db.session.commit()
      flash('Record was successfully added')
      return redirect(url_for('show_all'))
  return render_template('new_student.html', form=form)


@app.route('/job/<stid>', methods = ['POST'])
def savejob(stid):
  form = JobForm()
  if form.validate_on_submit():
    job = Job(request.form['name'], stid)
    db.session.add(job)
    db.session.commit()
    flash('Record was successfully added')
  return redirect(url_for('show_all'))


@app.route('/job/<stid>', methods=['GET'])
def createjob(stid):
  form = JobForm()
  student = db.session.get(Student, stid)
  return render_template('new_job.html', student=student, form=form)


if __name__ == '__main__':
  app.run(debug = True)