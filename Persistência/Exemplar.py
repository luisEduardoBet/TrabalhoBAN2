class Exemplar:
    def __init__(self):
        self.__idExemplar = -1
        self.__ehReserva = False
        self.__estaEmprestado = False
        self.__idLivro = -1

    # Setters
    def idExemplar(self, idExemplar):
        self.__idExemplar = idExemplar
        return self
    
    def ehReserva(self, ehReserva):
        self.__ehReserva = ehReserva
        return self
    
    def estaEmprestado(self, estaEmprestado):
        self.__estaEmprestado = estaEmprestado
        return self
    
    def idLivro(self, idLivro):
        self.__idLivro = idLivro
        return self
    
    # Getters
    def get_idExemplar(self):
        return self.__idExemplar
    
    def get_ehReserva(self):
        return self.__ehReserva
    
    def get_estaEmprestado(self):
        return self.__estaEmprestado
    
    def get_idLivro(self):
        return self.__idLivro
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__idExemplar = tupla[0]
        self.__ehReserva = tupla[1]
        self.__estaEmprestado = tupla[2]
        self.__idLivro = tupla[3]

        return self
    
    # __repr__
    def __repr__(self):
        return u"({}, {}, {}, {})".format(self.__idExemplar, self.__ehReserva, self.__estaEmprestado, self.__idLivro)