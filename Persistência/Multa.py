class Multa:
    def __init__(self):
        self.__idMulta = -1
        self.__valor = -1.0
        self.__idUsuario = -1

    # Setters
    def idMulta(self, idMulta):
        self.__idMulta = idMulta
        return self
    
    def valor(self, valor):
        self.__valor = valor
        return self
    
    def idUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
        return self
    
    # Getters
    def get_idMulta(self):
        return self.__idMulta
    
    def get_valor(self):
        return self.__valor
    
    def get_idUsuario(self):
        return self.__idUsuario
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__idMulta = tupla[0]
        self.__valor = tupla[1]
        self.__idUsuario = tupla[2]

    # __repr__
    def __repr__(self):
        return u"({}, {}, {})".format(self.__idMulta, self.__valor, self.__idUsuario)