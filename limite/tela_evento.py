from limite.tela import Tela
from datetime import datetime, timedelta


class TelaEvento(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_menu_inicial(self):
        print("------ Modulo de Eventos------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Evento")
        print("2 - Listar Eventos")
        print("3 - Ver Evento")
        print("0 - Voltar")

    def mostrar_menu_visualizacao(self):
        print("------ Menu de Detalhes ------")
        print("Escolha sua opção:")
        print("1 - Alterar")
        print("2 - Remover")
        print("3 - Gerenciar Participantes")
        print("4 - Gerenciar Organizadores")
        print("5 - Gerenciar Registros de Presença")
        print("0 - Voltar")

    def mostrar_menu_visualizacao_registro(self):
        print("------ Visualização de Registro ------")
        print("Escolha sua opção:")
        print("1 - Alterar")
        print("2 - Remover")
        print("0 - Voltar")

    def mostrar_menu_listar(self):
        print("Escolha sua opção:")
        print("1 - Ver todos")
        print("2 - Ver Eventos Futuros")
        print("3 - Ver Eventos Realizados")
        print("4 - Ordenar Por Participantes")
        print("0 - Voltar")

    def mostrar_menu_listar_participantes(self):
        print("Escolha sua opção:")
        print("1 - Ver todos os participantes")
        print("2 - Ver participantes a confirmar")
        print("3 - Ver participantes confirmados")
        print("0 - Voltar")

    def mostrar_menu_participantes(self):
        print("------ Menu de Participantes ------")
        print("Escolha sua opção:")
        print("0 - Voltar")
        print("1 - Adicionar participante")
        print("2 - Remover participante")
        print("3 - Listar Participantes")
        print("4 - Confirmar participante")

    def mostrar_menu_organizadores(self):
        print("------ Menu de Organizadores ------")
        print("Escolha sua opção:")
        print("0 - Voltar")
        print("1 - Adicionar organizador")
        print("2 - Remover Organizador")
        print("3 - Listar Organizadores")

    def mostrar_menu_confirmar_participantes(self):
        print("------ Menu de Confirmação ------")
        print("Escolha sua opção:")
        print("1 - Confirmar com vacina")
        print("2 - Confirmar com exame")

    def mostrar_menu_registros(self):
        print("------ Menu de Registros de Presença ------")
        print("Escolha sua opção:")
        print("0 - Voltar")
        print("1 - Listar Registros")
        print("2 - Ver Registro")
        print("3 - Registrar Presença")
        print("4 - Registrar Saída")

    def mostrar(self, evento, i):
        print(i, "-", evento.titulo, "-",
              evento.data.strftime("%d/%m/%Y - %H:%M"))

    def mostrar_detalhes(self, evento):
        print("------ Visualizar evento ------")
        print("Nome: {}".format(evento.titulo))
        print("Data: {}".format(evento.data.strftime("%d/%m/%Y - %H:%M")))

        self.mostrar_endereco(evento.local)

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Evento ------") if not alterar else print(
            "------ Alterar Evento ------")

        evento = {}

        evento["titulo"] = self.ler_string(
            "Informe o título do evento: ", self.validar_string(min=3, max=50))

        evento["data"] = self.ler_data("Data do evento (use o formato dd/mm/aaaa): ",
                                       self.validar_data(min=datetime(year=2019, month=1, day=1)))

        horario = self.ler_horario(
            "Informe o horário do evento (use o formato hh:mm): ")

        evento["data"] = evento["data"] + \
            timedelta(hours=horario.hour, minutes=horario.minute)

        if(evento["data"] < datetime.today()):
            print("Atenção: você está cadastrando um evento que já ocorreu.")

        if(not alterar):
            evento["capacidade"] = self.ler_inteiro(
                "Informe a capacidade máxima do evento: ", self.validar_inteiro(min=1))

        evento["endereco"] = self.mostrar_tela_endereco()

        return evento

    def mostrar_registro(self, registro, i):
        print(i, registro.participante.nome)

    def mostrar_detalhes_registro(self, registro):
        print("------ Visualizar registro ------")
        print("Participante", registro.participante.nome)
        print("Entrada:", registro.entrada.data.strftime("%d/%m/%Y - %H:%M"))
        if(registro.saida):
            print("Saída:", registro.saida.data.strftime("%d/%m/%Y - %H:%M"))

    def mostrar_tela_registrar_presenca(self, data_evento, limite, entrada=True):

        print("------ Registrar entrada ------" if entrada else "------ Registrar saída ------")

        limite_inferior = data_evento - limite
        limite_superior = data_evento + limite

        data = self.ler_data("Informe a data:")
        if(data < limite_inferior or data > limite_superior):
            raise ValueError(
                "A data informada deve ser, no máximo, um dia após ou antes do evento.")

        while(True):
            horario = self.ler_horario("Informe o horário:")

            data = data + timedelta(hours=horario.hour, minutes=horario.minute)
            if(data < data_evento):
                confirmacao = self.confirmar(
                    "A data/horário informado é anterior ao do evento. Deseja prosseguir mesmo assim? (s/n)")
                if(confirmacao):
                    break
            else:
                break

        return data
