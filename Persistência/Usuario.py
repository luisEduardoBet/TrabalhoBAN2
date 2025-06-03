class Usuario:
    def __init__(self):
        self.__idUsuario = -1
        self.__nome = ''
        self.__endereco = ''
        self.__telefone = ''
        self.__numEmprestimos = -1
        self.__idCategoria = -1

    # Setters
    def idUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
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
    
    def numEmprestimos(self, numEmprestimos):
        self.__numEmprestimos = numEmprestimos
        return self
    
    def idCategoria(self, idCategoria):
        self.__idCategoria = idCategoria
        return self
    
    # Getters
    def get_idUsuario(self):
        return self.__idUsuario
    
    def get_nome(self):
        return self.__nome
    
    def get_endereco(self):
        return self.__endereco
    
    def get_telefone(self):
        return self.__telefone
    
    def get_numEmprestimos(self):
        return self.__numEmprestimos
    
    def get_idCategoria(self):
        return self.__idCategoria
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__idUsuario = tupla[0]
        self.__nome = tupla[1]
        self.__endereco = tupla[2]
        self.__telefone = tupla[3]
        self.__numEmprestimos = tupla[4]
        self.__idCategoria = tupla[5]

    # __repr__
    def __repr__(self):
        return u"({}, {}, {}, {}, {}, {})".format(self.__idUsuario, self.__nome, self.__endereco, self.__telefone, self.__numEmprestimos, self.__idCategoria)