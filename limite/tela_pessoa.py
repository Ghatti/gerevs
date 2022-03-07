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
            [sg.Text("Nome:", size=(15, 1)), sg.InputText(key="nome")],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText(key="cpf")],
            [sg.Text("Nascimento:", size=(15, 1)), sg.InputText(
                key="nascimento"), sg.CalendarButton("Nascimento", target="nascimento", format="%d/%m/%Y")],
            [sg.Text("CEP:", size=(15, 1)), sg.InputText(key="cep")],
            [sg.Text("Rua:", size=(15, 1)), sg.InputText(key="rua")],
            [sg.Text("Número:", size=(15, 1)), sg.InputText(key="numero")],
            [sg.Text("Bairro:", size=(15, 1)), sg.InputText(key="bairro")],
            [sg.Text("Cidade:", size=(15, 1)), sg.InputText(key="cidade")],
            [sg.Text("Estado:", size=(15, 1)), sg.InputText(key="estado")],
            [sg.Submit("Enviar"), sg.Cancel("Cancelar")]
        ]

        self.window = sg.Window(
            "Cadastrar Pessoa", default_element_size=(40, 1)).Layout(layout)

    def ler_cpf(self):
        return self.ler_string(
            "Informe o cpf (Utilize o formato 000.000.000-00): ", self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"))

    def mostrar_tela_cadastro(self, alterar=False):

        self.init_tela_cadastro()
        button, values = self.open()
        self.close()

        values["numero"] = int(values["numero"])
        values["nascimento"] = datetime.strptime(
            values["nascimento"], "%d/%m/%Y")

        self.self_validar_cadastro(values)

        return values

    def mostrar_tela_cadastro_repetido(self, pessoa):
        self.mostrar_mensagem(
            "Já existe uma pessoa cadastrada com esse CPF")
        self.mostrar_detalhes(pessoa)
        return self.ler_string(
            "Deseja prosseguir com essa pessoa? (s/n) ", self.validar_string(opcoes=("s", "n"))).lower() == "s"

    def self_validar_cadastro(self, dados):

        validator_dispatch = {
            "nome": self.validar_string(min=2, max=31, no_digit=True),
            "cpf": self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"),
            "nascimento": self.validar_data(max=datetime.today(), delta=timedelta(days=150*365)),
            "cep": self.validar_string(formato=r"^\d{2}\.\d{3}\-\d{3}$"),
            "numero": self.validar_inteiro(min=0),
            "bairro": self.validar_string(no_digit=True),
            "cidade": self.validar_string(no_digit=True),
            "estado": self.validar_string(no_digit=True)
        }

        for key in validator_dispatch.keys():
            validators = validator_dispatch[key]

            for validator_func in validators:
                validator_func(dados[key])
