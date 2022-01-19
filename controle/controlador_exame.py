from entidade.exame import Exame
from controle.controlador import Controlador
from limite.tela_exame import TelaExame


class ControladorExame(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaExame(self))

    def abrir_menu_visualizacao(self, exame):
        opcoes = {1: self.cadastrar}
        opcoes_validas = [0, 1]
        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes, opcoes_validas, exame)

    def cadastrar(self):

        dados = self.tela.mostrar_tela_cadastro()

        return Exame(dados["data"], dados["resultado"])

    def mostrar(self, exame):
        self.tela.mostrar_exame(exame)
        self.abrir_menu_visualizacao(exame)
