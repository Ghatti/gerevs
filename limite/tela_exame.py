import PySimpleGUI as sg
from limite.tela import Tela
from datetime import datetime, timedelta, time


class TelaExame(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

    def init_lista(self, exames):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Lista de Exames",
                     size=(30, 1), font=("Helvetica", 25))],
            [sg.Table([[exame["data"], exame["resultado"]] for exame in exames],  headings=["Data", "Resultado"
                                                                                            ], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button("Cadastrar", key=1), sg.Button("Alterar", key=2), sg.Button(
                "Remover", key=3), sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Exames", default_element_size=(40, 1)).Layout(layout)

    def init_tela_cadastro(self, values, alterar=False):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Data:", size=(15, 1)), sg.InputText(values["data"] if values else None,
                                                          key="data"), sg.CalendarButton("Calendário", target="nascimento", format="%d/%m/%Y")],
            [sg.Text("Horário:", size=(15, 1)), sg.InputText(values["horario"] if values else None,
                                                             key="horario")],
            [sg.Text("Resultado:", size=(15, 1)), sg.Radio(
                "Positivo", "resultado"), sg.Radio("Negativo", "resultado", default=True)]

            [sg.Submit("Enviar", key="enviar"),
             sg.Cancel("Cancelar", key=0)]
        ]

        self.window = sg.Window(
            "Cadastrar Exame", default_element_size=(40, 1)).Layout(layout)

    def mostrar_tela_cadastro(self, default_values=None, alterar=False):

        values = default_values

        while(True):
            try:
                self.init_tela_cadastro(values, alterar)
                button, values = self.open()
                self.close()

                if(button == 0):
                    return

                self.validar_cadastro(values)

                try:
                    horario = time.fromisoformat(values["horario"])
                except ValueError:
                    raise ValueError(
                        "O horário informado não é válido. Utilize o formato hh:mm.")

            except ValueError as err:
                self.mostrar_mensagem(err, "Erro")

        exame["data"] = exame["data"] + \
            timedelta(hours=horario.hour, minutes=horario.minute)
        return exame

    def mostrar_menu_visualizacao(self):
        print("------ Menu de Exame ------")
        print("Escolha sua opção:")
        print("1 - Registrar exame")
        print("0 - Voltar")

    def mostrar(self, exames):

        self.init_lista(exames)
        button, values = self.open()
        self.close()
        return button, values

    def validar_cadastro(self, dados):

        validator_dispatch = {
            "data": self.validar_data(min=datetime(year=2019, month=1, day=1), max=datetime.today()),
            "horario": self.validar_string(formato=r"^\d{2}\:\d{2}$")
        }

        for key in validator_dispatch.keys():
            validator_dispatch[key](dados[key])
