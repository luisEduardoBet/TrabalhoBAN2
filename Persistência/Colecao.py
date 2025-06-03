class Colecao:
    def __init__(self):
        self.__idColecao = -1
        self.__nome = ''

    # Setters
    def idColecao(self, idColecao):
        self.__idColecao = idColecao
        return self
    
    def nome(self, nome):
        self.__nome = nome
        return self
    
    # Getters
    def get_idColecao(self):
        return self.__idColecao
    
    def get_nome(self):
        return self.__nome
    

    # from_tupla
    def from_tupla(self, tupla):
        self.__idColecao = tupla[0]
        self.__nome = tupla[1]

        return self
    
    # __repr__
    def __repr__(self):
        return u"({}, {})".format(self.__idColecao, self.__nome)