from pessoa import Pessoa
from endereco import Endereco

class Organizador(Pessoa):

    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: Endereco):

        super().__init__(cpf, nome, nascimento, endereco)