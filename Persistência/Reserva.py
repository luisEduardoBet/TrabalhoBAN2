import datetime as dt
class Reserva:
    def __init__(self):
        self.__idReserva = -1
        self.__idUsuario = -1
        self.__idExemplar = -1
        self.__dataReserva = dt.date(2000, 1, 1)
        self.__hora = dt.time(0, 0, 0)

    # Setters
    def idReserva(self, idReserva):
        self.__idReserva = idReserva
        return self
    
    def idUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
        return self
    
    def idExemplar(self, idExemplar):
        self.__idExemplar = idExemplar
        return self
    
    def dataReserva(self, dataReserva):
        self.__dataReserva = dataReserva
        return self
    
    def hora(self, hora):
        self.__hora = hora
        return self
    
    # Getters
    def get_idReserva(self):
        return self.__idReserva
    
    def get_idUsuario(self):
        return self.__idUsuario
    
    def get_idExemplar(self):
        return self.__idExemplar
    
    def get_dataReserva(self):
        return self.__dataReserva
    
    def get_hora(self):
        return self.__hora
    
    # from_tupla
    def from_tupla(self, tupla):
        self.__idReserva = tupla[0]
        self.__idUsuario = tupla[1]
        self.__idExemplar = tupla[2]
        self.__dataReserva = tupla[3]
        self.__hora = tupla[4]

        return self
    
    # __repr__
    def __repr__(self):
        return u"({}, {}, {}, {}, {})".format(self.__idReserva, self.__idUsuario, self.__idExemplar, self.__dataReserva, self.__hora)