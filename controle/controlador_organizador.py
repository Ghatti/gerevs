from controle.controlador_integrante import ControladorIntegrante
from limite.tela_organizador import TelaOrganizador
from dao.organizador_dao import OrganizadorDAO


class ControladorOrganizador(ControladorIntegrante):

    def __init__(self, controlador_sistema, controlador_pessoa):
        super().__init__(controlador_sistema, controlador_pessoa,
                         TelaOrganizador(self), OrganizadorDAO())
