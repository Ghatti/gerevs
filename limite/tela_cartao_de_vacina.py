from limite.tela import Tela


class TelaCartaoDeVacina(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_tela_cadastro(self):

        print("------ Cadastrar Cartão de Vacina ------")

        dose1 = self.ler_string(
            "A primeira dose já foi aplicada? s/n", "Valor inválido").strip().lower()
        dose2 = self.ler_string(
            "A segunda dose já foi aplicada? s/n", "Valor inválido").strip().lower()

        return [dose1 == "s", dose2 == "s"]

    def mostrar_menu_visualizacao(self):
        print("------ Menu de Cartão de Vacinas ------")
        print("Escolha sua opção:")
        print("1 - Registrar dose")
        print("0 - Voltar")

    def mostrar_detalhes(self, cartao):

        print("------ Cadastrar Cartão de Vacina ------")
        print("Dose 1: {}".format(cartao.doses[0]))
        print("Dose 2: {}".format(cartao.doses[1]))
