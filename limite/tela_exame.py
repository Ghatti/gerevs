import PySimpleGUI as sg
from exceptions.validationException import ValidationException
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
            [sg.Button("Cadastrar", key=1), sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Exames", default_element_size=(40, 1)).Layout(layout)

    def init_tela_selecao(self, exames):
        sg.ChangeLookAndFeel('Reddit')

        table = self.generate_table(exames)

        layout = [table, [sg.Ok(key="ok")]]

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
                "Positivo", "resultado", key="positivo"), sg.Radio("Negativo", "resultado", default=True, key="negativo")],
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

                self.validar_cadastro(values)

                try:
                    horario = time.fromisoformat(values["horario"])
                except ValueError:
                    raise ValidationException(
                        "O horário informado não é válido. Utilize o formato hh:mm.")

                data = datetime.strptime(
                    values["data"], "%d/%m/%Y") + timedelta(hours=horario.hour, minutes=horario.minute)

                return {
                    "data": data,
                    "resultado": values["positivo"]
                }

            except ValueError as err:
                self.mostrar_mensagem(err, "Erro")

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

    def generate_table(self, opcoes):

        return [sg.Table([[exame["data"], exame["resultado"]] for exame in opcoes],  headings=["Data", "Resultado"
                                                                                               ], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE)]
