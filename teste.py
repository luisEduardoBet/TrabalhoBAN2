from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
  pass


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/biblioteca'

db = SQLAlchemy()
db.init_app(app)


db.reflect()

class User(db.Model):
     '''deal with an existing table'''
     __table__ = db.Model.metadata.tables['bibliotecario']


u = User.query.all()
print(u[0])

@app.route("/")
def welcome(): 
    return render_template("login.html")

@app.route("/register")
def register(): 
    return render_template("register.html")

app.run(debug=True)