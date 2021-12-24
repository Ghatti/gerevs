class Evento:

    def __init__(self, titulo: str, data: str, horario: str, local, capacidade: int, organizador):

        self.__titulo = titulo
        self.__data = data
        self.__horario = horario
        self.__local = local
        self.__capacidade = capacidade
        self.__organizadores = [organizador]
        self.__participantes_a_confirmar = []
        self.__participantes_confirmados = []

    @property
    def titulo(self):
        return self.titulo

    @property
    def data(self):
        return self.data

    @property
    def horario(self):
        return self.horario

    @property
    def local(self):
        return self.local

    @property
    def capacidade(self):
        return self.capacidade

    @property
    def organizadores(self):
        return self.organizadores

    @property
    def participantes_a_confirmar(self):
        return self.participantes_a_confirmar

    @property
    def participantes_confirmados(self):
        return self.participantes_confirmados

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @data.setter
    def data(self, data: str):
        self.__data = data

    @horario.setter
    def horario(self, horario: str):
        self.__horario = horario

    @local.setter
    def local(self, local: str):
        self.__local = local

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    def adicionar_organizador(self, organizador):
        pass

    def remover_organizador(self, organizador):
        pass

    def adicionar_participante(self, participante):
        pass

    def remover_participante(self, participante):
        pass

    def confirmar_participante(self, participante):
        pass
