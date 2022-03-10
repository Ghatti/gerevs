from dao.abstract_dao import AbstractDAO
from entidade.pessoa import Pessoa


class PessoaDAO(AbstractDAO):

    def __init__(self, caminho):

        super().__init__(caminho)

    def persist(self, pessoa: Pessoa):
        if(self.__pessoa_valida(pessoa)):
            super().persist(pessoa.cpf, pessoa)

    def remove(self, pessoa: Pessoa):
        if(self.__pessoa_valida(pessoa)):
            super().remove(pessoa.cpf)

    def __pessoa_valida(self, pessoa):
        return (pessoa is not None) and (isinstance(pessoa, Pessoa) and isinstance(pessoa.cpf, str))
