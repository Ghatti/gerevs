from controle.controlador import Controlador
from limite.tela_cartao_de_vacina import TelaCartaoDeVacina
from entidade.cartao_de_vacina import CartaoDeVacina


class ControladorCartaoDeVacina(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaCartaoDeVacina(self))

    def cadastrar(self):

        doses = self.tela.mostrar_tela_cadastro()
        return CartaoDeVacina(doses)

    def mostrar(self, cartao):

        self.tela.mostrar_detalhes(cartao)


    def registrar_dose(self, cartao=CartaoDeVacina):

        cartao.registrar_dose()
        self.tela.mostrar_mensagem("Dose registrada!")
