from limite.tela import Tela

class TelaCartaoDeVacina(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_tela_cadastro(self):

        print("------ Cadastrar Cartão de Vacina ------")

        dose1 = self.ler_string("A primeira dose já foi aplicada? s/n").strip().lower()
        dose2 = self.ler_string("A segunda dose já foi aplicada? s/n").strip().lower()

        return (dose1 == "s", dose2 == "s")

