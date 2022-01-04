from limite.tela import Tela


class TelaParticipante(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_menu_inicial(self):
        print("------ Modulo de Participantes ------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Participante")
        print("2 - Listar Participantes")
        print("3 - Ver Participante")
        print("0 - Voltar")