from flask import Flask, render_template, request, flash, redirect, url_for, session, g
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from sqlalchemy import text
from models.database import db
from models.models import Bibliotecario, Usuario
import datetime


app = Flask(__name__)
app.secret_key = "123123"
lg_manager = LoginManager(app)
lg_manager.login_view = "login"
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/biblioteca'
db.init_app(app)




@lg_manager.user_loader
def user_loader(id): 
  tabela = session.get('table')

  if tabela == 1: 
    bib = db.session.query(Bibliotecario).filter_by(id_bibliotecario=id).first()
    return bib
  
  elif tabela == 2: 
    user = db.session.query(Usuario).filter_by(id_usuario=id).first()
    return user
  else: 
    return None

  


@app.route("/home", methods = ["GET", "POST"])
@login_required
def home():

  if request.method == "POST": 

    pesquisa = request.form["pesquisa"]

    
    if (pesquisa == ''): 
    
      resultado = db.session.execute(
        text('SELECT isbn, esta_emprestado, id_exemplar FROM livro join exemplar using(id_livro) WHERE eh_reserva = false')
      ).fetchall()
      
      return render_template("home.html", resultado = resultado)

  return render_template("home.html")

  
@app.route("/efetivar_emprestimo", methods=["GET", "POST"])
@login_required
def emprestimo():

  if request.method == "POST": 

    exemplares = request.form.getlist('checkbox')
    data = str(datetime.date.today())
    id = current_user.get_id()
    for exemplar in exemplares: 

       db.session.execute(
         text("INSERT INTO emprestimo (id_exemplar, id_usuario ,data_inicio) VALUES ({},{},'{}')".format(exemplar, id, data))
      )
      
    db.session.commit()

      


  return redirect(url_for("home"))
    


@app.route("/perfil", methods = ["GET", "POST"])
@login_required
def profile(): 

  if request.method == "GET": 
    query = text(r'SELECT * from emprestimo WHERE id_usuario = :val')
    resultado = db.session.execute(query, {"val": current_user.get_id()}).fetchall()

    return render_template("perfil.html", resultado = resultado)




@app.route("/", methods = ["GET", "POST"])
def login():

  if request.method == "GET":
      return render_template("login.html")

  else: 
    cpf = request.form["cpf"]
    senha = request.form["senha"]
    tipo_usuario = request.form["tipo_usuario"]

    print(tipo_usuario)

    user = None
    if tipo_usuario == "1":
      user =  db.session.query(Bibliotecario).filter_by(cpf = cpf, senha = senha).first()
      session['table'] = 1

    elif tipo_usuario == "3": 
      user =  db.session.query(Usuario).filter_by(cpf = cpf, senha = senha).first()
      session['table'] = 2
      

    if user: 
        login_user(user)
        return redirect(url_for("home"))
    
    return redirect(url_for("login"))
    


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
    
    elif tipo_usuario == "2": 
      user = Usuario(cpf = cpf, 
                     nome = nome, 
                     senha = password, 
                     endereco = endereco,
                     telefone = telefone) 
      db.session.add(user)
      db.session.commit()

      session['table'] = 2
      login_user(user)

      return redirect(url_for("home"))

      
  return render_template("register.html")

app.run(debug=True)