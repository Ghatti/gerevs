import PySimpleGUI as sg
from limite.tela_integrante import TelaIntegrante


class TelaParticipante(TelaIntegrante):

    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_detalhes(self, pessoa):
        self.init_detalhes(pessoa, participante=True)
        button, values = self.open()

        self.close()
        return button, values

    def mostrar_tela_erro_exame(self):

        registrar = self.ler_string(
            "Participante não possui exame cadastrado. Deseja registrar um exame?", self.validar_string(opcoes=["n", "s"])).strip().lower()

        return registrar == "s"
