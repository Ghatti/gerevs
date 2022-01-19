from entidade.exame import Exame
from controle.controlador import Controlador
from limite.tela_exame import TelaExame


class ControladorExame(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaExame(self))
