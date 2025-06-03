class Livro:
    def __init__(self):
        self.__idLivro = -1
        self.__isbn = ''
        self.__idColecao = -1
        self.__idEditora = -1

    # Setters
    def idLivro(self, idLivro):
        self.__idLivro = idLivro
        return self
    
    def isbn(self, isbn):
        self.__isbn = isbn
        return self
    
    def idColecao(self, idColecao):
        self.__idColecao = idColecao
        return self
    
    def idEditora(self, idEditora):
        self.__idEditora = idEditora
        return self
    
    # Getters
    def get_idLivro(self):
        return self.__idLivro
    
    def get_isbn(self):
        return self.__isbn
    
    def get_idColecao(self):
        return self.__idColecao
    
    def get_idEditora(self):
        return self.__idEditora
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__idLivro = tupla[0]
        self.__isbn = tupla[1]
        self.__idColecao = tupla[2]
        self.__idEditora = tupla[3]

        return self
    
    # __repr__
    def __repr__(self):
        return u"({}, {}, {}, {})".format(self.__idLivro, self.__isbn, self.__idColecao, self.__idEditora)
    