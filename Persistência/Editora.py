class Editora:
    def __init__(self):
        self.__idEditora = -1
        self.__nome = ''
        self.__endereco = ''

    # Setters
    def idEditora(self, idEditora):
        self.__idEditora = idEditora
        return self
    
    def nome(self, nome):
        self.__nome = nome
        return self
    
    def endereco(self, endereco):
        self.__endereco = endereco
        return self
    
    # Getters
    def get_idEditora(self):
        return self.__idEditora
    
    def get_nome(self):
        return self.__nome
    
    def get_endereco(self):
        return self.__endereco
    

    # from_tupla
    def from_tupla(self, tupla):
        self.__idEditora = tupla[0]
        self.__nome = tupla[1]
        self.__endereco = tupla[2]

        return self
    
    
    # __repr__
    def __repr__(self):
        return u"({}, {}, {})".format(self.__idEditora, self.__nome, self.__endereco)