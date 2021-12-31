from entidade.pessoa import Pessoa
from entidade.endereco import Endereco


class Organizador(Pessoa):

    def __init__(self, cpf: str, nome: str, nascimento: str, endereco):

        super().__init__(cpf, nome, nascimento, Endereco(endereco["cep"], endereco["rua"], endereco["numero"],
                                                         endereco["bairro"], endereco["cidade"], endereco["estado"]))
