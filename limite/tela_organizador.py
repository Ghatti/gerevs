from limite.tela import Tela


class TelaOrganizador(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_menu_inicial(self):
        print("------ Modulo de Organizadores ------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Organizador")
        print("0 - Encerrar Sistema")
