from entidade.exame import Exame
from controle.controlador import Controlador
from limite.tela_exame import TelaExame


class ControladorExame(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaExame(self))

    def abrir_menu_visualizacao(self, registrar_exame):
        opcoes = {1: registrar_exame}
        opcoes_validas = [0, 1]
        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes, opcoes_validas)

    def cadastrar(self):

        dados = self.tela.mostrar_tela_cadastro()
        exame = Exame(dados["data"], dados["resultado"])
        self.tela.mostrar_detalhes(exame)
        return exame

    def mostrar(self, exame, registrar_exame):
        self.tela.mostrar_detalhes(exame)
        self.abrir_menu_visualizacao(registrar_exame)
