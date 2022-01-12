from entidade.organizador import Organizador
from entidade.participante import Participante
from entidade.endereco import Endereco


class Evento:

    def __init__(self, titulo: str, data: str, horario: str, endereco, capacidade: int, organizador: Organizador):

        self.__titulo = titulo
        self.__data = data
        self.__horario = horario
        self.__local = Endereco(endereco["cep"], endereco["rua"], endereco["numero"],
                                endereco["bairro"], endereco["cidade"], endereco["estado"])
        self.__capacidade = capacidade
        self.__organizadores = [organizador]
        self.__participantes_a_confirmar = []
        self.__participantes_confirmados = []

    @property
    def titulo(self):
        return self.__titulo

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def local(self):
        return self.__local

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def organizadores(self):
        return self.__organizadores

    @property
    def participantes_a_confirmar(self):
        return self.__participantes_a_confirmar

    @property
    def participantes_confirmados(self):
        return self.__participantes_confirmados

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
    def local(self, local: Endereco):
        self.__local = local

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    def adicionar_organizador(self, organizador: Organizador):
        pass

    def remover_organizador(self, organizador: Organizador):
        pass

    def adicionar_participante(self, participante: Participante):
        pass

    def remover_participante(self, participante: Participante):
        pass

    def confirmar_participante(self, participante: Participante):
        pass
