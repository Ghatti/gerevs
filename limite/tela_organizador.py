from limite.tela import Tela


class TelaOrganizador(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_menu_inicial(self):
        print("------ Modulo de Organizadores ------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Organizador")
        print("0 - Encerrar Sistema")

        opcoes = [1]
        while True:
            opcao = input("Escolha a opcao:")

            try:
                opcao = int(opcao)
                if(opcao not in opcoes):
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor incorreto. Digite um valor numérico válido.")                    