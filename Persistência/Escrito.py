class Escrito:
    def __init__(self):
        self.__idAutor = -1
        self.__idLivro = -1

    # Setters
    def idAutor(self, idAutor):
        self.__idAutor = idAutor
        return self
    
    def idLivro(self, idLivro):
        self.__idLivro = idLivro
        return self
    
    # Getters
    def get_idAutor(self):
        return self.__idAutor
    
    def get_idLivro(self):
        return self.__idLivro
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__idAutor = tupla[0]
        self.__idLivro = tupla[1]

        return self
    
    # __repr__
    def __repr__(self):
        return u"({}, {})".format(self.__idAutor, self.__idLivro)
    