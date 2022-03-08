import PySimpleGUI as sg
from limite.tela_integrante import TelaIntegrante


class TelaParticipante(TelaIntegrante):

    def __init__(self, controlador):

        super().__init__(controlador)

 #   def mostrar_menu_visualizacao(self):
#
 #       print("------ Menu de Detalhes ------")
 #       print("Escolha sua opção:")
 #       print("1 - Alterar")
 #       print("2 - Remover")
 #       print("3 - Ver Cartão de Vacinas")
 #       print("4 - Ver Exame")
 #       print("0 - Voltar")

    def mostrar_detalhes(self, pessoa):
        self.init_detalhes(pessoa, participante=True)
        button, values = self.open()

        print(button)

        self.close()
        return button, values

    def mostrar_tela_erro_exame(self):

        registrar = self.ler_string(
            "Participante não possui exame cadastrado. Deseja registrar um exame?", self.validar_string(opcoes=["n", "s"])).strip().lower()

        return registrar == "s"
