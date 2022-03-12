from dao.pessoa_dao import PessoaDAO
from entidade.pessoa import Pessoa


class OrganizadorDAO(PessoaDAO):

    def __init__(self):

        super().__init__("organizadores.pkl")
