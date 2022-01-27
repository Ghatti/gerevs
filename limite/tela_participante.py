from limite.tela_pessoa import TelaPessoa

class TelaParticipante(TelaPessoa):

    def __init__(self, controlador):

        super().__init__(controlador)


    def mostrar_menu_visualizacao(self):
        print("------ Menu de Detalhes ------")
        print("Escolha sua opção:")
        print("1 - Alterar")
        print("2 - Remover")
        print("3 - Ver Cartão de Vacinas")
        print("4 - Ver Exame")
        print("0 - Voltar")


    def mostrar_tela_erro_exame(self):

        registrar = self.ler_string(
            "Participante não possui exame cadastrado. Deseja registrar um exame? s/n", self.validar_string(opcoes=["n", "s"])).strip().lower()

        return registrar == "s"
