from controle.controlador import Controlador
from limite.tela_cartao_de_vacina import TelaCartaoDeVacina
from entidade.cartao_de_vacina import CartaoDeVacina


class ControladorCartaoDeVacina(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaCartaoDeVacina(self))

    def abrir_menu_visualizacao(self, cartao):
        opcoes = {1: self.registrar_dose}
        opcoes_validas = [0, 1]
        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes, opcoes_validas, cartao)

    def cadastrar(self):

        doses = self.tela.mostrar_tela_cadastro()
        return CartaoDeVacina(doses)

    def mostrar(self, cartao):

        self.tela.mostrar_detalhes(cartao)
        self.abrir_menu_visualizacao(cartao)

    def registrar_dose(self, cartao=CartaoDeVacina):

        if(not cartao.is_complete()):
            cartao.registrar_dose()
            self.tela.mostrar_mensagem("Dose registrada!")
        else:
            self.tela.mostrar_mensagem(
                "O esquema de vacinação já está completo.")
