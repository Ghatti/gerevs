import PySimpleGUI as sg
from controle.controlador import Controlador
from limite.tela_integrante import TelaIntegrante
from datetime import datetime, timedelta


class TelaPessoa(TelaIntegrante):

    def __init__(self, controlador: Controlador):

        super().__init__(controlador)

    def init_tela_cadastro(self):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Nome:", size=(15, 1)), sg.InputText()],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText()],
            # this will not work read about target
            [sg.Text("Nascimento:", size=(15, 1)), sg.InputText(
                key="calendar"), sg.CalendarButton("Nascimento", target="calendar")],
            [sg.Text("CEP:", size=(15, 1)), sg.InputText()],
            [sg.Text("Número:", size=(15, 1)), sg.InputText()],
            [sg.Text("Bairro:", size=(15, 1)), sg.InputText()],
            [sg.Text("Cidade:", size=(15, 1)), sg.InputText()],
            [sg.Text("Estado:", size=(15, 1)), sg.InputText()],
            [sg.Submit("Enviar"), sg.Cancel("Cancelar")]
        ]

        self.window = sg.Window(
            "Cadastrar Pessoa", default_element_size=(40, 1)).Layout(layout)

    def ler_cpf(self):
        return self.ler_string(
            "Informe o cpf (Utilize o formato 000.000.000-00): ", self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"))

    def mostrar_tela_cadastro(self, alterar=False):
        # print("------ Cadastrar ------") if not alterar else print(
        #    "------ Alterar ------")
        #
        #pessoa = {}
        # pessoa["nome"] = self.ler_string(
        #    "Informe o nome: ", self.validar_string(min=2, max=31, no_digit=True))
        # pessoa["nascimento"] = self.ler_data("Data de nascimento (use o formato dd/mm/aaaa): ",
        #                                     self.validar_data(max=datetime.today(), delta=timedelta(days=150*365)))
        #pessoa["endereco"] = self.mostrar_tela_endereco()

        self.init_tela_cadastro()
        button, values = self.open()
        self.close()

        return values

    def mostrar_tela_cadastro_repetido(self, pessoa):
        self.mostrar_mensagem(
            "Já existe uma pessoa cadastrada com esse CPF")
        self.mostrar_detalhes(pessoa)
        return self.ler_string(
            "Deseja prosseguir com essa pessoa? (s/n) ", self.validar_string(opcoes=("s", "n"))).lower() == "s"
