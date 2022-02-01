from limite.tela import Tela


class TelaCartaoDeVacina(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_menu_visualizacao(self):
        print("------ Menu de Cartão de Vacinas ------")
        print("Escolha sua opção:")
        print("1 - Registrar dose")
        print("0 - Voltar")

    def mostrar_detalhes(self, cartao):

        print("------ Cadastrar Cartão de Vacina ------")
        print("Dose 1: {}".format(
            "Aplicada." if cartao.doses[0] else "Pendente"))
        print("Dose 2: {}".format(
            "Aplicada." if cartao.doses[1] else "Pendente"))
