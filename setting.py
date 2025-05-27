import psycopg as postgres


class Connection: 

    __instance = None 
    __connection = None


    def __new__(cls): 
        
        if cls.__instance is None: 
            cls.__instance = super().__new__(cls)
            cls.__connection = postgres.connect( 

                host = 'localhost', dbname = 'biblioteca' , user = 'postgres', password  = 'postgres'
                
            )
            
            return cls.__instance
        
    def cursor(self): 

        return self.__connection.cursor()

    
    def commit(self):
        self.__connection.commit()
    

    def close(self): 
        return self.__connection.close()
    


class Bibliotecario:  
    
    def __init__(self): 
        self.__id  = -1 
        self.__cpf  = ''
        self.__nome = ''
        self.__endereco = '' 
        self.__telefone = ''


 #Setters 
    def id(self, id): 
        self.__id =  id 
        return self
    
    def cpf(self, cpf): 
        self.__cpf = cpf
        return self
    
    def nome(self, nome): 
        self.__nome = nome
        return self
    
    def endereceo(self, endereco): 
        self.__endereco = endereco
        return self
    
    def telefone(self, telefone): 
        self.__telefone = telefone
        return self
    
#Getters 

    def get_id(self): 
        return self.__id
    
    def get_cpf(self): 
        return self.__cpf
    
    def get_nome(self):
        return self.__nome
    
    def get_endereco(self): 
        return self.__endereco
    
    def get_telefone(self):
        return self.__telefone


    def from_tupla(self, tupla): 

        self.__id =  tupla[0]
        self.__cpf  = tupla[1]
        self.__nome = tupla[2]
        self.__endereco = tupla[3]
        self.__telefone = tupla[4]

        return self 
    

    def __repr__(self):
        
        return u"({}, {}, {}, {}, {})".format(self.__id, self.__cpf, self.__nome, self.__endereco, self.__telefone)
    


class BibliotecarioDAO:

    def __init___(self):  

        self.asda = None

    def select_all(self) -> list: 

        con = Connection()
        cursor = con.cursor()
        cursor.execute( 'select * from bibliotecario')

        result = cursor.fetchall()

        biblio = []

        for i in result:
            biblio.append(Bibliotecario().from_tupla(i))

        return biblio
    



def main(): 
    bibliotecario = BibliotecarioDAO()

    biblios = bibliotecario.select_all() 

    for i in biblios: 
        print(i)



main()