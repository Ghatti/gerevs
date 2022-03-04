import PySimpleGUI as sg
from limite.tela_gui import TelaGui


class TelaMenuInicialGui(TelaGui):

    def __init__(self, entidades):
        self.init_components(entidades)

    def init_components(self, entidades):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Listbox(values=entidades, size=(30, 3))],
            [sg.Text("Menu Inicial",
                     size=(30, 1), font=("Helvetica", 25))],
            [sg.Button("Cadastrar", key=1), sg.Button("Alterar", key=2), sg.Button("Remover", key=4), sg.Button(
                "Ver Detalhes", key=3), sg.Button("Voltar", key=0)]

        ]

        self.window = sg.Window(
            "Menu Inicial", default_element_size=(40, 1)).Layout(layout)
