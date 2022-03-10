import PySimpleGUI as sg
from limite.tela import Tela
from datetime import datetime, timedelta, time


class TelaEvento(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def init_menu_inicial(self, entidades):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Módulo de Eventos",
                     size=(30, 1), font=("Helvetica", 25))],
            [sg.Table([[entidade["titulo"], entidade["data"], entidade["participantes_total"]] for entidade in entidades],  headings=["Título", "Data",
                      "Participantes"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button("Ver Eventos Futuros", key=4), sg.Button(
                "Ver Eventos Realizados", key=5), sg.Button("Ver Ranking", key=6)],
            [sg.Button("Cadastrar", key=1), sg.Button("Alterar", key=2), sg.Button(
                "Remover", key=4), sg.Button("Ver Detalhes", key=3), sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Módulo de Eventos", default_element_size=(40, 1)).Layout(layout)

    def init_tela_listar(self, event_list, titulo):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            event_list,
            [sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            titulo, default_element_size=(40, 1)).Layout(layout)

    def init_detalhes(self, evento):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Título: ", size=(15, 1)), sg.Text(evento["titulo"])],
            [sg.Text("Data: ", size=(15, 1)),
             sg.Text(evento["data"])],
            [sg.Text("Horário: ", size=(15, 1)),
             sg.Text(evento["horario"])],
            [sg.Text("Capacidade: ", size=(15, 1)),
             sg.Text(evento["capacidade"])],
            [sg.Text("Endereço", size=(15, 1))],
            [sg.Text("CEP: ", size=(15, 1)), sg.Text(evento["cep"])],
            [sg.Text("Rua: ", size=(15, 1)), sg.Text(evento["rua"])],
            [sg.Text("Número: ", size=(15, 1)), sg.Text(evento["numero"])],
            [sg.Text("Bairro: ", size=(15, 1)), sg.Text(evento["bairro"])],
            [sg.Text("Cidade: ", size=(15, 1)), sg.Text(evento["cidade"])],
            [sg.Text("Estado: ", size=(15, 1)), sg.Text(evento["estado"])],
            [sg.Button("Participantes", key=1), sg.Button(
                "Organizadores", key=2), sg.Button("Registros de Presença", key=3), sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Detalhes", default_element_size=(40, 1)).Layout(layout)

    def init_tela_cadastro(self, values, alterar=False):

        sg.ChangeLookAndFeel('Reddit')

        layout = [

            [sg.Text("Título:", size=(15, 1)), sg.InputText(
                values["titulo"] if values else None, key="titulo")],
            [sg.Text("Data:", size=(15, 1)), sg.InputText(values["data"] if values else None,
                                                          key="data"), sg.CalendarButton("Calendário", target="data", format="%d/%m/%Y")],
            [sg.Text("Horário:", size=(15, 1)), sg.InputText(
                values["horario"] if values else None, key="horario")],
            [sg.Text("Capacidade:", size=(15, 1)), sg.InputText(
                values["capacidade"] if values else None, key="capacidade", disabled=alterar)],
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
            "Cadastrar Evento", default_element_size=(40, 1)).Layout(layout)

    def init_menu_organizadores(self, org_list):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            org_list,
            [sg.Button("Adicionar", key=1), sg.Button(
                "Remover", key=2), sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Gerenciar Organizadores", default_element_size=(40, 1)).Layout(layout)

    def init_menu_participantes(self, part_list):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            part_list,
            [sg.Button(
                "Participantes Confirmados", key=3), sg.Button("Participantes a confirmar", key=4)],
            [sg.Button("Adicionar", key=1),  sg.Button(
                "Remover", key=2), sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Gerenciar Participantes", default_element_size=(40, 1)).Layout(layout)

    def init_tela_lista_participantes(self, part_list, confirmar=False):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            part_list,
            [sg.Button("Confirmar com Vacina", key=1),  sg.Button(
                "Confirmar com exame", key=2), sg.Button("Voltar", key=0)] if confirmar else [sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Participantes confirmados" if not confirmar else "Participantes a confirmar", default_element_size=(40, 1)).Layout(layout)

    def init_tela_registros(self, registros):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Registros de Presença",
                     size=(30, 1), font=("Helvetica", 25))],
            [sg.Table([[entidade["participante"], entidade["entrada"], entidade["saida"]] for entidade in registros],  headings=["Participante", "Entrada",
                      "Saída"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button("Registrar Entrada", key=1), sg.Button("Registrar Saída", key=2), sg.Button(
                "Alterar", key=3), sg.Button("Remover", key=4), sg.Button("Voltar", key=0)]
        ]

        self.window = sg.Window(
            "Registros de Presença", default_element_size=(40, 1)).Layout(layout)

    def init_tela_registrar_presenca(self, values):
        sg.ChangeLookAndFeel('Reddit')

        layout = [[sg.Text("Data:", size=(15, 1)), sg.InputText(values["data"] if values else None,
                                                                key="data"), sg.CalendarButton("Calendário", target="data", format="%d/%m/%Y")],
                  [sg.Text("Horário:", size=(15, 1)), sg.InputText(
                      values["horario"] if values else None, key="horario")],
                  [sg.Ok(), sg.Button("Voltar", key=0)]]

        self.window = sg.Window(
            "Registros de Presença", default_element_size=(40, 1)).Layout(layout)

    def mostrar_menu_inicial(self, entidades):

        self.init_menu_inicial(entidades)
        button, values = self.open()
        self.close()
        return button, values

    def mostrar_tela_listar(self, event_list=[], titulo="Lista de eventos"):

        self.init_tela_listar(event_list, titulo)
        button, values = self.open()
        self.close()
        return button, values

    def mostrar_tela_listar_participantes(self, part_list, confirmar=False):
        self.init_tela_lista_participantes(part_list, confirmar)
        button, values = self.open()
        self.close()

        if(button == 0):
            return button, None

        if(len(values["row_index"]) == 0):
            raise ValueError(
                "É necessário escolher um participante para confirmar")

        return button, values

    def mostrar_menu_participantes(self, part_list):
        self.init_menu_participantes(part_list)
        button, values = self.open()
        self.close()

        if(button == 0):
            return button, None

        if(button == 2 and len(values["row_index"]) == 0):
            raise ValueError(
                "É necessário escolher um participante para remover")

        return button, values

    def mostrar_menu_organizadores(self, org_list):
        self.init_menu_organizadores(org_list)
        button, values = self.open()
        self.close()

        if(button == 0):
            return button, None

        if(button == 2 and len(values["row_index"]) == 0):
            raise ValueError(
                "É necessário escolher um organizador para remover")

        return button, values

    def mostrar_menu_registros(self, registros):

        self.init_tela_registros(registros)
        button, values = self.open()
        self.close()

        if(button == 0):
            return button, None

        if(button != 1 and len(values["row_index"]) == 0):
            raise ValueError(
                "É necessário escolher um registro.")

        return button, values

    def mostrar_detalhes(self, evento):
        self.init_detalhes(evento)
        button, values = self.open()
        self.close()
        return button, values

    def mostrar_tela_cadastro(self, default_values=None, alterar=False):

        values = default_values

        while(True):
            try:
                self.init_tela_cadastro(values, alterar)
                button, values = self.open()
                self.close()

                if(button == 0):
                    raise StopIteration("Cadastro Cancelado")

                self.validar_cadastro(values)

                try:
                    horario = time.fromisoformat(values["horario"])
                except ValueError:
                    raise ValueError(
                        "O horário informado não é válido. Utilize o formato hh:mm.")

                values["data"] = datetime.strptime(
                    values["data"], "%d/%m/%Y") + timedelta(hours=horario.hour, minutes=horario.minute)
                values["capacidade"] = int(values["capacidade"])

                return values
            except ValueError as err:
                self.mostrar_mensagem(err, "Erro")

    def mostrar_tela_registrar_presenca(self, data_evento, limite, default_values=None):

        values = default_values
        limite_inferior = data_evento - limite
        limite_superior = data_evento + limite

        while True:
            try:
                self.init_tela_registrar_presenca(values)

                button, values = self.open()
                self.close()

                if(button == 0):
                    raise ValueError("Registro cancelado")

                try:
                    horario = time.fromisoformat(values["horario"])
                except ValueError:
                    raise ValueError(
                        "O horário informado não é válido. Utilize o formato hh:mm.")

                values["data"] = datetime.strptime(
                    values["data"], "%d/%m/%Y") + timedelta(hours=horario.hour, minutes=horario.minute)

                if(values["data"] < limite_inferior or values["data"] > limite_superior):
                    raise ValueError(
                        "A data informada deve ser, no máximo, um dia após ou antes do evento.")

                return values

            except ValueError as err:
                self.mostrar_mensagem(err, "Erro")

    def validar_cadastro(self, dados):

        validator_dispatch = {
            "titulo": self.validar_string(min=3, max=50),
            "capacidade": self.validar_inteiro(min=1),
            "data": self.validar_data(min=datetime(year=2019, month=1, day=1)),
            "cep": self.validar_string(formato=r"^\d{2}\.\d{3}\-\d{3}$"),
            "numero": self.validar_inteiro(min=0),
            "bairro": self.validar_string(no_digit=True),
            "cidade": self.validar_string(no_digit=True),
            "estado": self.validar_string(no_digit=True)
        }

        for key in validator_dispatch.keys():
            validator_dispatch[key](dados[key])

    def generate_table(self, opcoes):

        return [sg.Table([[entidade["titulo"], entidade["data"], entidade["participantes_total"]] for entidade in opcoes],  headings=["Título", "Data",
                                                                                                                                      "Participantes"], key="row_index", select_mode=sg.TABLE_SELECT_MODE_BROWSE)]
