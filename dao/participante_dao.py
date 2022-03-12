from dao.pessoa_dao import PessoaDAO
from entidade.pessoa import Pessoa


class ParticipanteDAO(PessoaDAO):

    def __init__(self):

        super().__init__("participantes.pkl")
