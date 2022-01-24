from entidade.registro_de_presenca import RegistroDeṔresenca
from controle.controlador import Controlador
from limite.tela_registro_de_presenca import TelaRegistroDePresenca


class ControladorExame(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaRegistroDePresenca(self))

    def inicializar(self):
        # mostrar lista de eventos já realizados
        # mostrar menu para selecionar evento
        # mostrar registros de presenca do evento selecionado
        # mostrar menu de registros de presenca
        pass
