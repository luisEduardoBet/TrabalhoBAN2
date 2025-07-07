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
  query = None
  if request.method == "POST": 

    pesquisa =  request.form['pesquisa']
    tipo_pesquisa = request.form['tipo_pesquisa']

   
        
    if tipo_pesquisa == "1":

      pipeline = [
                { "$lookup":{ 
                    "from": "livro",
                    "localField": "livro",
                    "foreignField" : "_id",
                    "as": "livro_exemplar"
                  }
                },

                {"$unwind" : "$livro_exemplar"},

                {"$group": {"_id": "$livro_exemplar.nome", "exemplares" : {"$sum": 1 }}}, 

                {"$project": {"Nome": "$_id", "Numero Exemplares": "$exemplares", "_id":0 }}
      ] 

      if pesquisa != '': 
        match_query = {"$match": {"livro_exemplar.nome": pesquisa}}
        pipeline.insert(2, match_query)      

          
      query = list(mongo.db.exemplar.aggregate(pipeline))

    
    elif tipo_pesquisa == "2": 
      pipeline = [

                { "$lookup":{ 
                    "from": "autor",
                    "localField": "autor",
                    "foreignField" : "_id",
                    "as": "autor_livro"
                  }
                },

                {"$unwind" : "$autor_livro"},

                {"$group": {"_id": "$autor_livro.nome", "livros" : {"$sum": 1 }}}, 

                {"$project": {"Nome": "$_id", "Livros Escritos": "$livros", "_id":0 }}
      ] 

      if pesquisa != '': 
        match_query = {"$match": {"autor_livro.nome": pesquisa}}
        pipeline.insert(2, match_query)      


      query  = list(mongo.db.livro.aggregate(pipeline))

    elif tipo_pesquisa == "3": 
      pipeline = [ 
                  
                  { "$lookup":{ 
                    "from": "colecao",
                    "localField": "colecao",
                    "foreignField" : "_id",
                    "as": "colecao_livro"
                  }
                },

                {"$unwind" : "$colecao_livro"},

                {"$group": {"_id": "$colecao_livro.nome", "livros" : {"$sum": 1 }}}, 

                {"$project": {"Nome": "$_id", "Livros da Colecao": "$livros", "_id":0 }}]


      if pesquisa != '': 
        match_query = {"$match": {"colecao_livro.nome": pesquisa}}
        pipeline.insert(2, match_query)     

      query  = list(mongo.db.livro.aggregate(pipeline))
      
    return render_template("home.html", resultado = query, tipo = tipo_pesquisa)

  return render_template("home.html")

@app.route("/emprestimo", methods=["GET", "POST"])
@login_required
def emprestimo():


  if request.method == "GET": 
    dado = request.args.get('dado')
    tipo = request.args.get('tipo')
    
    if tipo == '1':
      pipeline = [
                  { "$lookup":{ 
                      "from": "livro",
                      "localField": "livro",
                      "foreignField" : "_id",
                      "as": "livro_exemplar"
                    }
                  },

                  {"$unwind" : "$livro_exemplar"},

                  {"$match": {"livro_exemplar.nome": dado}},

                  {"$project": {"Nome": "$livro_exemplar.nome", "Exemplar:": "$_id", 
                                "Emprestado": "$esta_emprestado", "Reserva:": "$eh_reserva", "_id":0 }}
                                  ] 
      
      query = list(mongo.db.exemplar.aggregate(pipeline))

      return render_template("emprestimo.html", resultado=query) 
    
    elif tipo == '2':
      pipeline = [

                { "$lookup":{ 
                    "from": "autor",
                    "localField": "autor",
                    "foreignField" : "_id",
                    "as": "autor_livro"
                  }
                },

                {"$unwind" : "$autor_livro"},

                {"$match": {"autor_livro.nome": dado}},

                { "$lookup":{ 
                    "from": "exemplar",
                    "localField": "_id",
                    "foreignField" : "livro",
                    "as": "livro_exemplar"
                  }
                },

                {"$unwind" : "$livro_exemplar"},


                {"$project": {"Nome": "$nome", "Exemplar": "$livro_exemplar._id", 
                                "Emprestado": "$livro_exemplar.esta_emprestado", 
                                "Reserva:": "$livro_exemplar.eh_reserva", "_id":0 }}
      ] 

      query  = list(mongo.db.livro.aggregate(pipeline))
      return render_template("emprestimo.html", resultado=query) 
    
    else:
      pipeline = [ 
                  
                  { "$lookup":{ 
                    "from": "colecao",
                    "localField": "colecao",
                    "foreignField" : "_id",
                    "as": "colecao_livro"
                  }
                },

                {"$unwind" : "$colecao_livro"},

                {"$match": {"colecao_livro.nome": dado}},

                { "$lookup":{ 
                    "from": "exemplar",
                    "localField": "_id",
                    "foreignField" : "livro",
                    "as": "livro_exemplar"
                  }
                },

                {"$unwind" : "$livro_exemplar"},


                {"$project": {"Nome": "$nome", "Exemplar": "$livro_exemplar._id", 
                                "Emprestado": "$livro_exemplar.esta_emprestado", 
                                "Reserva:": "$livro_exemplar.eh_reserva", "_id":0 }}]
  
      query  = list(mongo.db.livro.aggregate(pipeline))
      return render_template("emprestimo.html", resultado=query) 

  else: 
    
    return render_template("home.html")

  

  # elif tipo == '2':

  # elif tipo == '3': 
    

  # else:
  #   return render_template("home.html")








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