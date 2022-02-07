from entidade.pessoa import Pessoa

from entidade.endereco import Endereco


class Evento:

    def __init__(self, titulo: str, data: str, endereco, capacidade: int, organizador: Pessoa):

        self.__titulo = titulo
        self.__data = data
        self.__local = Endereco(endereco["cep"], endereco["rua"], endereco["numero"],
                                endereco["bairro"], endereco["cidade"], endereco["estado"])
        self.__capacidade = capacidade
        self.__organizadores = [organizador]
        self.__participantes_a_confirmar = []
        self.__participantes_confirmados = []
        self.__registros_de_presenca = []

    @property
    def titulo(self):
        return self.__titulo

    @property
    def data(self):
        return self.__data

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

    @property
    def registros_de_presenca(self):
        return self.__registros_de_presenca

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @data.setter
    def data(self, data: str):
        self.__data = data

    @local.setter
    def local(self, endereco):
        self.__local = Endereco(endereco["cep"], endereco["rua"], endereco["numero"],
                                endereco["bairro"], endereco["cidade"], endereco["estado"])

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    def get_all_participantes(self):
        return self.participantes_a_confirmar + self.participantes_confirmados

    def adicionar_registro_de_presenca(self, registro):

        self.registros_de_presenca.append(registro)

    def remover_registro_de_presenca(self, registro):

        self.registros_de_presenca.remove(registro)

    def adicionar_organizador(self, organizador: Pessoa):
        self.organizadores.append(organizador)

    def remover_organizador(self, organizador: Pessoa):
        self.organizadores.remove(organizador)

    def adicionar_participante(self, participante: Pessoa):
        self.participantes_a_confirmar.append(participante)

    def remover_participante(self, participante: Pessoa):
        self.participantes_a_confirmar.remove(
            participante) if participante in self.participantes_a_confirmar else self.participantes_confirmados.remove(participante)

    def confirmar_participante(self, participante: Pessoa):
        self.participantes_a_confirmar.remove(participante)
        self.participantes_confirmados.append(participante)
