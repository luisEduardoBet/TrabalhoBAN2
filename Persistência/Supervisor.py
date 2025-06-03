class Supervisor:
    def __init__(self):
        self.__idAssistente = -1
        self.__idBibliotecario = -1

    # Setters
    def idAssistente(self, idAssistente):
        self.__idAssistente = idAssistente
        return self
    
    def idBibliotecario(self, idBibliotecario):
        self.__idBibliotecario = idBibliotecario
        return self
    

    # Getters
    def get_idAssistente(self):
        return self.__idAssistente
    
    def get_idBibliotecario(self):
        return self.__idBibliotecario
    

    # from_tupla
    def from_tupla(self, tupla):
        self.__idAssistente = tupla[0]
        self.__idBibliotecario = tupla[1]

        return self
    
    # __repr__
    def __repr__(self):
        return u"({}, {})".format(self.__idAssistente, self.__idBibliotecario)