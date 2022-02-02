from entidade.cartao_de_vacina import CartaoDeVacina
from entidade.endereco import Endereco


class Pessoa():

    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: dict):

        self.__cpf = cpf
        self.__nome = nome
        self.__nascimento = nascimento
        self.__endereco = Endereco(endereco["cep"], endereco["rua"], endereco["numero"],
                                   endereco["bairro"], endereco["cidade"], endereco["estado"])
        self.__cartao_de_vacina = CartaoDeVacina()
        self.__exames = []

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def nascimento(self):
        return self.__nascimento

    @property
    def endereco(self):
        return self.__endereco

    @property
    def cartao_de_vacina(self):
        return self.__cartao_de_vacina

    @property
    def exames(self):
        return self.__exames

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @nascimento.setter
    def nascimento(self, nascimento: str):
        self.__nascimento = nascimento

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = Endereco(endereco["cep"], endereco["rua"], endereco["numero"],
                                   endereco["bairro"], endereco["cidade"], endereco["estado"])

    def add_exame(self, exame):

        if exame not in self.exames:
            self.exames.append(exame)
