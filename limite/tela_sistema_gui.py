import PySimpleGUI as sg
from limite.tela_gui import TelaGui


class TelaSistemaGui(TelaGui):

    def __init__(self):
        self.init_components()

    def init_components(self):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Sistema de Gerenciamento de Eventos",
                     size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Selecione um módulo para iniciar",
                     size=(30, 1), font=("Helvetica", 15))],
            [sg.Button("Eventos", key=1)],
            [sg.Button("Organizadores", key=2)],
            [sg.Button("Participantes", key=3)],
            [sg.Button("Sair", key=0)],
        ]

        self.window = sg.Window(
            "Menu Inicial", default_element_size=(40, 1)).Layout(layout)
