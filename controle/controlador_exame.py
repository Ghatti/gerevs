from entidade.exame import Exame
from controle.controlador import Controlador
from limite.tela_exame import TelaExame


class ControladorExame(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaExame(self))

    def abrir_menu_visualizacao(self, participante):
        opcoes = {1: self.registrar_exame}
        opcoes_validas = [0, 1]
        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes, opcoes_validas, participante)

    def registrar_exame(self, participante):
        # not happy with this
        # Quick workoround, will change this class overall to avoid this
        participante.exame = self.cadastrar()

    def cadastrar(self):

        dados = self.tela.mostrar_tela_cadastro()

        return Exame(dados["data"], dados["resultado"])

    def mostrar(self, participante):
        self.tela.mostrar_detalhes(participante.exame)
        self.abrir_menu_visualizacao(participante)
