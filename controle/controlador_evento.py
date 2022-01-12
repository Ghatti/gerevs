from entidade.evento import Evento
from entidade.endereco import Endereco
from controle.controlador import Controlador
from limite.tela_evento import TelaEvento


class ControladorEvento(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaEvento(self))

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar, 2: self.listar, 3: self.ver_detalhes}
        opcoes_validas = [0, 1, 2, 3]
        menu = self.tela.mostrar_menu_inicial

        self.listar()
        self.abrir_menu(menu, opcoes, opcoes_validas)


    def cadastrar(self):

        #if no organizador = mensagem nenhum organizador cadastrado

        dados = self.tela.mostrar_tela_cadastro()
        print(dados)