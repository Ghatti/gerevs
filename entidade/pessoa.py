from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: str):

        self.__cpf = cpf
        self.__nome = nome
        self.__nascimento = nascimento
        self.__endereco = endereco #placeholder - vai mudar

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
    def cpf(self):
        return self.__cpf

    @nome.setter
    @property
    def nome(self):
        return self.__nome

    @nascimento.setter
    @property
    def nascimento(self):
        return self.__nascimento

    @endereco.setter
    @property
    def endereco(self):
        return self.__endereco                        
        