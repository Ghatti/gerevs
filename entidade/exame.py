class Exame:

    def __init__(self, data: str, resultado: bool):
        self.__data = data
        self.__resultado = resultado

    @property
    def data(self):
        return self.__data

    @property
    def resultado(self):
        return self.__resultado
