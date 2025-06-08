from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models.database import db
from models.models import Bibliotecario, Usuario


app = Flask(__name__)
app.secret_key = "123123"
lg_manager = LoginManager(app)
lg_manager.login_view = "login"
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/biblioteca'
db.init_app(app)




@lg_manager.user_loader
def user_loader(id): 
  table = session.get("user_id")


  user = db.session.query(Bibliotecario).filter_by(id_bibliotecario=id).first()
  return user
  


@app.route("/home")
@login_required
def home(): 
  return render_template("home.html")


@app.route("/", methods = ["GET", "POST"])
def login():

  if request.method == "GET": 

      return render_template("login.html")

  else: 
    cpf = request.form["cpf"]
    senha = request.form["senha"]

    user =  db.session.query(Bibliotecario).filter_by(cpf = cpf, senha = senha).first()

    login_user(user)
    return redirect(url_for("home"))


@app.route("/logout")
@login_required
def logout(): 
  logout_user()
  return redirect(url_for("login"))
    

@app.route("/register", methods=["GET", "POST"])
def register(): 

  if request.method == "POST": 
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    endereco = request.form.get("endereco")
    telefone = request.form.get ("telefone")
    tipo_usuario = request.form.get("tipo")
    password = request.form.get("senha")

    if tipo_usuario == "1": 

        bib = Bibliotecario(cpf = cpf, nome = nome, senha = password, endereco = endereco, telefone = telefone)
        db.session.add(bib)
        db.session.commit()

        session['table'] = 1
        login_user(bib)

        return redirect(url_for("home"))
      
  return render_template("register.html")

app.run(debug=True)