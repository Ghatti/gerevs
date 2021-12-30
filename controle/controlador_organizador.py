from entidade.organizador import Organizador
from controle.controlador import Controlador
from limite.tela_organizador import TelaOrganizador


class ControladorOrganizador(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaOrganizador(self))

    def ver_eventos(self, organizador):
        pass

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar}
        opcoes_validas = [0, 1]
        menu = self.tela.mostrar_menu_inicial

        self.abrir_menu(menu, opcoes, opcoes_validas)

    def cadastrar(self):

        dados = self.tela.mostrar_tela_cadastro()
        
        #Procurar se há organizador com o cpf
        #criar organizador
        #incluir organizador
        print(dados)
        

    #move function to parent class
    def abrir_menu(self, menu = None, opcoes = {}, opcoes_validas = []):

        while True:
            menu()
            opcao_escolhida = self.tela.ler_inteiro(opcoes_validas)
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()
        

