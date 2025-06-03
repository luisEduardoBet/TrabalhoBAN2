class Autor:
    def __init__(self):
        self.__idAutor = -1
        self.__nome = ''

    # Setters
    def idAutor(self, idAutor):
        self.__idAutor = idAutor
        return self
    
    def nome(self, nome):
        self.__nome = nome
        return self
    
    # Getters
    def get_idAutor(self):
        return self.__idAutor
    
    def get_nome(self):
        return self.__nome
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__idAutor = tupla[0]
        self.__nome = tupla[1]

    # __repr__
    def __repr__(self):
        return u"({}, {})".format(self.__idAutor, self.__nome)