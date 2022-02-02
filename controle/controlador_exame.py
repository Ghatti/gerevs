from entidade.exame import Exame
from controle.controlador import Controlador
from limite.tela_exame import TelaExame


class ControladorExame(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaExame(self))

    def abrir_menu_visualizacao(self, registrar_exame):
        opcoes = {1: registrar_exame}

        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes)

    def cadastrar(self):

        dados = self.tela.mostrar_tela_cadastro()
        exame = Exame(dados["data"], dados["resultado"])
        return exame

    def mostrar_exames(self, exame, i):
        self.tela.mostrar(i+1, exame)

    def mostrar(self, exames, registrar_exame):
        try:

            self.listar(exames)

        except ValueError as err:
            self.tela.mostrar_mensagem(err)
        finally:
            self.abrir_menu_visualizacao(registrar_exame)
