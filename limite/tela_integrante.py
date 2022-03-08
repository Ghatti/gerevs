import PySimpleGUI as sg
from abc import ABC, abstractmethod
from limite.tela import Tela


class TelaIntegrante(Tela, ABC):

    @abstractmethod
    def __init__(self, controlador):

        super().__init__(controlador)

    def init_menu_inicial(self, entidades):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Menu Inicial",
                     size=(30, 1), font=("Helvetica", 25))],
            [sg.Table([[entidade["nome"], entidade["cpf"], entidade["nascimento"]] for entidade in entidades],  headings=["Nome", "CPF",
                      "Nascimento"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button("Cadastrar", key=1), sg.Button("Alterar", key=2), sg.Button("Remover", key=4), sg.Button(
                "Ver Detalhes", key=3), sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Menu Inicial", default_element_size=(40, 1)).Layout(layout)

    def init_detalhes(self, pessoa, participante=False):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Nome: ", size=(15, 1)), sg.Text(pessoa["nome"])],
            [sg.Text("CPF: ", size=(15, 1)), sg.Text(pessoa["cpf"])],
            [sg.Text("Nascimento: ", size=(15, 1)),
             sg.Text(pessoa["nascimento"])],
            [sg.Text("Vacinas: ")] if participante else [],
            [sg.Text("Dose 1: ", size=(15, 1)), sg.Text(
                pessoa["vacina"][0])] if participante else [],
            [sg.Text("Dose 2: ", size=(15, 1)), sg.Text(
                pessoa["vacina"][1])] if participante else [],
            [sg.Text("Endereço", size=(15, 1))],
            [sg.Text("CEP: ", size=(15, 1)), sg.Text(pessoa["cep"])],
            [sg.Text("Rua: ", size=(15, 1)), sg.Text(pessoa["rua"])],
            [sg.Text("Número: ", size=(15, 1)), sg.Text(pessoa["numero"])],
            [sg.Text("Bairro: ", size=(15, 1)), sg.Text(pessoa["bairro"])],
            [sg.Text("Cidade: ", size=(15, 1)), sg.Text(pessoa["cidade"])],
            [sg.Text("Estado: ", size=(15, 1)), sg.Text(pessoa["estado"])],
            [sg.Button("Registrar Vacina", key=1), sg.Button(
                "Registrar Ver Exames", key=2), sg.Button("Voltar", key=0)] if participante else [sg.Ok()]
        ]

        self.window = sg.Window(
            "Detalhes", default_element_size=(40, 1)).Layout(layout)

    def mostrar_menu_inicial(self, entidades):
        self.init_menu_inicial(entidades)
        button, values = self.open()
        self.close()
        return button, values

    def mostrar_detalhes(self, pessoa):
        self.init_detalhes(pessoa)
        button, values = self.open()
        self.close()
        return button, values
