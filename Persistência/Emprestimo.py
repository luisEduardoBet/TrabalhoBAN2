import datetime as dt

class Emprestimo:
    def __init__(self):
        self.__idEmprestimo = -1
        self.__idExemplar = -1
        self.__idUsuario = -1
        self.__dataInicio = dt.date(2000, 1, 1)
        self.__dataFim = dt.date(2000, 1, 1)
        self.__numRenovacoes = -1
        self.__estaAtrasado = False

    # Setters
    def idEmprestimo(self, idEmprestimo):
        self.__idEmprestimo = idEmprestimo
        return self
    
    def idExemplar(self, idExemplar):
        self.__idExemplar = idExemplar
        return self
    
    def idUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
        return self
    
    def dataInicio(self, dataInicio):
        self.__dataInicio = dataInicio
        return self
    
    def dataFim(self, dataFim):
        self.__dataFim = dataFim
        return self
    
    def numRenovacoes(self, numRenovacoes):
        self.__numRenovacoes = numRenovacoes
        return self
    
    def estaAtrasado(self, estaAtrasado):
        self.__estaAtrasado = estaAtrasado
        return self
    
    # Getters
    def get_idEmprestimo(self):
        return self.__idEmprestimo
    
    def get_idExemplar(self):
        return self.__idExemplar
    
    def get_idUsuario(self):
        return self.__idUsuario
    
    def get_dataInicio(self):
        return self.__dataInicio
    
    def get_dataFim(self):
        return self.__dataFim
    
    def get_numRenovacoes(self):
        return self.__numRenovacoes
    
    def get_estaAtrasado(self):
        return self.__estaAtrasado
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__idEmprestimo = tupla[0]
        self.__idExemplar = tupla[1]
        self.__idUsuario = tupla[2]
        self.__dataInicio = tupla[3]
        self.__dataFim = tupla[4]
        self.__numRenovacoes = tupla[5]
        self.__estaAtrasado = tupla[6]

        return self
    
    # __repr__
    def __repr__(self):
        return u"({}, {}, {}, {}, {}, {}, {})".format(self.__idEmprestimo, self.__idExemplar, self.__idUsuario, self.__dataInicio, self.__dataFim, self.__numRenovacoes, self.__estaAtrasado)