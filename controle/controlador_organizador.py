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
            self.tela.mostrar_menu_inicial()
            opcoes_validas = [0, 1]
            opcao_escolhida = self.tela.ler_inteiro(opcoes_validas)
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()


        

