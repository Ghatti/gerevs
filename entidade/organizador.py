from entidade.pessoa import Pessoa
from entidade.endereco import Endereco

class Organizador(Pessoa):

    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: Endereco):

        super().__init__(cpf, nome, nascimento, endereco)