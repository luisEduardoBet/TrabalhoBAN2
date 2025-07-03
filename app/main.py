from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from models.models import User


app = Flask(__name__)
app.secret_key = "123123"
lg_manager = LoginManager(app)
lg_manager.login_view = "login"
app.config['MONGO_URI'] = "mongodb://localhost:27017/biblioteca"
mongo =  PyMongo(app)



@lg_manager.user_loader
def user_loader(id): 
  t_user = session.get('user_type')

  if t_user == 3: 
    user =  mongo.db.usuario.find_one({"_id": ObjectId(id)})
    return User(user); 

  elif t_user == 2: 
    user =  mongo.db.assistente.find_one({"_id": ObjectId(id)})
    return User(user); 

  else:
    user =  mongo.db.bibliotecario.find_one({"_id": ObjectId(id)})
    return User(user); 







@app.route("/home", methods = ["GET", "POST"])
@login_required
def home():
  
  if request.method == "POST": 
    pipeline = [

      { "$lookup":{ 
          "from": "livro",
          "localField": "livro",
          "foreignField" : "_id",
          "as": "livro_exemplar"
        }
      },

      {"$unwind" : "$livro_exemplar"},

      {"$project": {"_id": 1, "nome": "$livro_exemplar.nome", "ISBN": "$livro_exemplar.ISBN"}}
    ]

    teste = list(mongo.db.exemplar.aggregate(pipeline))
  
    return render_template("home.html", resultado = teste)

  return render_template("home.html")

@app.route("/efetivar_emprestimo", methods=["GET", "POST"])
@login_required
def emprestimo():

  return redirect(url_for("home"))






@app.route("/perfil", methods = ["GET", "POST"])
@login_required
def profile(): 

  return render_template("perfil.html", resultado = None)




@app.route("/", methods = ["GET", "POST"])
def login():

  if request.method == "GET":
      return render_template("login.html")

  else: 
    cpf = request.form["cpf"]
    senha = request.form["senha"]
    tipo_usuario = request.form["tipo_usuario"]


    user = None

    #Usuario Comum
    if tipo_usuario == "3":  
      user =  mongo.db.usuario.find_one({"$and":[{"CPF": cpf}, {"senha":  senha}]})
      session['user_type'] = 3
      

    #Assistente
    elif tipo_usuario == "2": 
      user = mongo.db.assistente.find_one({"$and":[{"CPF": cpf}, {"senha":  senha}]})
      session['user_type'] = 2

    #Bibliotecario
    else:
      user = mongo.db.bibliotecario.find_one({"$and":[{"CPF": cpf}, {"senha":  senha}]})     
      session['user_type'] = 1

    if user: 
      login_user(User(user))
      return redirect(url_for("home"))
    
    return redirect(url_for("login"))
    


@app.route("/logout")
@login_required
def logout(): 
  logout_user()
  return redirect(url_for("login"))
    

@app.route("/register", methods=["GET", "POST"])
def register():   
  error = None
  if request.method == "POST":
    data = request.form.to_dict()
    user_type = data.pop('tipo')

    if user_type == '3': 
      
      someone = mongo.db.usuario.find_one({"CPF": data['cpf']})

      if not someone: 
        mongo.db.usuario.insert_one(data)
        session['user_type'] = 3
        login_user(User(data))
        return redirect(url_for("home"))
      else: 
        error = "Usuario já existente!! CPF já existe"

      

    elif user_type == '2': 
        
      someone = mongo.db.assistente.find_one({"CPF": data['cpf']})

      if not someone: 
        mongo.db.assistente.insert_one(data)
        session['user_type'] = 2
        login_user(User(data))
        return redirect(url_for("home"))
      else: 
        error = "Usuario já existente!! CPF já existe"
        

    
    else:
      someone =  mongo.db.bibliotecario.find_one({"CPF": data['cpf']})
    
      if not someone: 
        mongo.db.bibliotecario.insert_one(data)
        session['user_type'] = 1
        login_user(User(data))
        return redirect(url_for("home"))
      
      else: 
        error = "Usuario já existente!! CPF já existe"

  return render_template("register.html", erro = error)




app.run(debug=True)