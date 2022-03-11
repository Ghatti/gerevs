import PySimpleGUI as sg
from controle.controlador import Controlador
from limite.tela_integrante import TelaIntegrante
from datetime import datetime, timedelta


class TelaPessoa(TelaIntegrante):

    def __init__(self, controlador: Controlador):

        super().__init__(controlador)

    def init_tela_cadastro(self, values, alterar=False):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Nome:", size=(15, 1)), sg.InputText(
                values["nome"] if values else None, key="nome")],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText(
                values["cpf"] if values else None, key="cpf", disabled=alterar)],
            [sg.Text("Nascimento:", size=(15, 1)), sg.InputText(values["nascimento"] if values else None,
                                                                key="nascimento"), sg.CalendarButton("Calendário", target="nascimento", format="%d/%m/%Y")],
            [sg.Text("CEP:", size=(15, 1)), sg.InputText(
                values["cep"] if values else None, key="cep")],
            [sg.Text("Rua:", size=(15, 1)), sg.InputText(
                values["rua"] if values else None, key="rua")],
            [sg.Text("Número:", size=(15, 1)), sg.InputText(
                values["numero"] if values else None, key="numero")],
            [sg.Text("Bairro:", size=(15, 1)), sg.InputText(
                values["bairro"] if values else None, key="bairro")],
            [sg.Text("Cidade:", size=(15, 1)), sg.InputText(
                values["cidade"] if values else None, key="cidade")],
            [sg.Text("Estado:", size=(15, 1)), sg.InputText(
                values["estado"] if values else None, key="estado")],
            [sg.Submit("Enviar", key="enviar"),
             sg.Cancel("Cancelar", key=0)]
        ]

        self.window = sg.Window(
            "Cadastrar Pessoa", default_element_size=(40, 1)).Layout(layout)

    def mostrar_tela_cadastro(self, organizadores=[], default_values=None, alterar=False):

        values = default_values

        while(True):
            try:
                self.init_tela_cadastro(
                    values, alterar)
                button, values = self.open()
                self.close()

                if(button == 0):
                    raise StopIteration("Cadastro/Alteração cancelado")

                self.validar_cadastro(values)
                values["nascimento"] = datetime.strptime(
                    values["nascimento"], "%d/%m/%Y")
                values["numero"] = int(values["numero"])

                return values
            except ValueError as err:
                self.mostrar_mensagem(err, "Erro")
            except StopIteration as err:
                self.mostrar_mensagem(err, "Erro")
                break

    def mostrar_tela_cadastro_repetido(self, pessoa):

        confirmar = sg.popup_yes_no(
            "Já existe uma pessoa cadastrada com o CPF {} chamada {}. Deseja continuar com essa pessoa?".format(pessoa["cpf"], pessoa["nome"]))

        return confirmar == "Yes"

    def validar_cadastro(self, dados):

        validator_dispatch = {
            "nome": self.validar_string(min=2, max=31, no_digit=True),
            "cpf": self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"),
            "nascimento": self.validar_data(max=datetime.today(), delta=timedelta(days=150*365)),
            "cep": self.validar_string(formato=r"^\d{2}\.\d{3}\-\d{3}$"),
            "numero": self.validar_inteiro(min=0),
            "rua": self.validar_string(min=1),
            "bairro": self.validar_string(min=1, no_digit=True),
            "cidade": self.validar_string(min=1, no_digit=True),
            "estado": self.validar_string(min=1, no_digit=True)
        }

        for key in validator_dispatch.keys():
            validator_dispatch[key](dados[key])
