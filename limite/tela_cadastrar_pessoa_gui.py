import PySimpleGUI as sg
from limite.tela_gui import TelaGui


class TelaCadastrarPessoaGui(TelaGui):
    def __init__(self):
        self.init_components()

    def init_components(self):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Nome:", size=(15, 1)), sg.InputText("nome")],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText("cpf")],
            # this will not work read about target
            [sg.Text("Nascimento:", size=(15, 1)), sg.InputText(
                key="calendar"), sg.CalendarButton("Nascimento", target="calendar")],
            [sg.Text("CEP:", size=(15, 1)), sg.InputText("cep")],
            [sg.Text("Número:", size=(15, 1)), sg.InputText("numero")],
            [sg.Text("Bairro:", size=(15, 1)), sg.InputText("bairro")],
            [sg.Text("Cidade:", size=(15, 1)), sg.InputText("cidade")],
            [sg.Text("Estado:", size=(15, 1)), sg.InputText("estado")],
            [sg.Submit("Enviar"), sg.Cancel("Cancelar")]
        ]

        self.window = sg.Window(
            "Cadastrar Pessoa", default_element_size=(40, 1)).Layout(layout)
