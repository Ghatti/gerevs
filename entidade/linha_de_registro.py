class LinhaDeRegistro:
    def __init__(self, data, horario):
        self.__data = data
        self.horario = horario

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @data.setter
    def data(self, data):
        self.__data = data

    @horario.setter
    def horario(self, horario):
        self.__horario = horario