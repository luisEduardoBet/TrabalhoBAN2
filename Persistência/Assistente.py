class Assistente:
    def __init__(self):
        self.__id = -1
        self.__cpf = ''
        self.__nome = ''
        self.__endereco = ''
        self.__telefone = ''

    # Setters
    def id(self, id):
        self.__id = id
        return self
    
    def cpf(self, cpf):
        self.__cpf = cpf
        return self
    
    def nome(self, nome):
        self.__nome = nome
        return self
    
    def endereco(self, endereco):
        self.__endereco = endereco
        return self
    
    def telefone(self, telefone):
        self.__telefone = telefone
        return self
    
    # Getters
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
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__id = tupla[0]
        self.__cpf = tupla[1]
        self.__nome = tupla[2]
        self.__endereco = tupla[3]
        self.__telefone = tupla[4]

        return self
    
    # __repr__
    def __repr__(self):
        return u"({}, {}, {}, {}, {})".format(self.__id, self.__cpf, self.__nome, self.__endereco, self.__telefone)