from controle.controlador import Controlador
from limite.tela_organizador import TelaOrganizador


class ControladorOrganizador(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaOrganizador(self))

    def ver_eventos(self, organizador):
        pass

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar}

        while True:
            opcao_escolhida = self.tela.mostrar_menu_inicial()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()

            opcoes = range(1)


        

