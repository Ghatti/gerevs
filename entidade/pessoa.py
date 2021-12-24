from abc import ABC, abstractmethod
from endereco import Endereco


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: Endereco):

        self.__cpf = cpf
        self.__nome = nome
        self.__nascimento = nascimento
        self.__endereco = endereco  # placeholder - vai mudar

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
    def endereco(self, endereco: Endereco):
        self.__endereco = endereco
