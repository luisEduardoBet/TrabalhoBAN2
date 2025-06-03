class Categoria:
    def __init__(self):
        self.__idCategoria = -1
        self.__nome = ''
        self.__tempoMaxEmprestimo = -1
        self.__numMaxEmprestimos = -1

    # Setters
    def idCategoria(self, idCategoria):
        self.__idCategoria = idCategoria
        return self
    
    def nome(self, nome):
        self.__nome = nome
        return nome
    
    def tempoMaxEmprestimo(self, tempoMaxEmprestimo):
        self.__tempoMaxEmprestimo = tempoMaxEmprestimo
        return self
    
    def numMaxEmprestimos(self, numMaxEmprestimos):
        self.__numMaxEmprestimos = numMaxEmprestimos
        return self
    
    # Getters
    def get_idCategoria(self):
        return self.__idCategoria
    
    def get_nome(self):
        return self.__nome
    
    def get_tempoMaxEmprestimo(self):
        return self.__tempoMaxEmprestimo
    
    def get_numMaxEmprestimos(self):
        return self.__numMaxEmprestimos
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__idCategoria = tupla[0]
        self.__nome = tupla[1]
        self.__tempoMaxEmprestimo = tupla[2]
        self.__numMaxEmprestimos = tupla[3]

    # __repr__
    def __repr__(self):
        return u"({}, {}, {}, {})".format(self.__idCategoria, self.__nome, self.__tempoMaxEmprestimo, self.__numMaxEmprestimos)