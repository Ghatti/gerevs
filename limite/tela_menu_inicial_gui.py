import PySimpleGUI as sg
from limite.tela_gui import TelaGui


class TelaMenuInicialGui(TelaGui):

    def __init__(self, entidades):
        self.init_components(entidades)

    def init_components(self, entidades):

        sg.ChangeLookAndFeel('Reddit')

        col = [[sg.Radio(entidade["nome"], "radio"), sg.Text(entidade["cpf"], size=(
            15, 1)), sg.Text(entidade["nascimento"], size=(15, 1))] for entidade in entidades]

        layout = [
            [sg.Text("Menu Inicial",
                     size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Nome", size=(15, 1)), sg.Text(
                "CPF", size=(15, 1)), sg.Text("Nascimento", size=(15, 1))],
            [sg.Column(col)],
            [sg.Button("Cadastrar", key=1), sg.Button("Alterar", key=2), sg.Button("Remover", key=4), sg.Button(
                "Ver Detalhes", key=3), sg.Button("Voltar", key=0)]


        ]

        self.window = sg.Window(
            "Menu Inicial", default_element_size=(40, 1)).Layout(layout)
