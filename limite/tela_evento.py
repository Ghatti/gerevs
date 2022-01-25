from limite.tela import Tela
from datetime import datetime, time


class TelaEvento(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_menu_inicial(self):
        print("------ Modulo de Eventos------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Evento")
        print("2 - Listar Eventos")
        print("3 - Ver Evento")
        print("4 - Ver Eventos Futuros")
        print("5 - Ver Eventos Realizados")
        print("0 - Voltar")

    def mostrar_menu_visualizacao(self):
        print("------ Menu de Detalhes ------")
        print("Escolha sua opção:")
        print("1 - Alterar")
        print("2 - Remover")
        print("3 - Ver Participantes")
        print("4 - Ver Organizadores")
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
        print("3 - Confirmar participante")
        print('4 - Gerenciar Registros')

    def mostrar_menu_organizadores(self):
        print("------ Menu de Organizadores ------")
        print("Escolha sua opção:")
        print("0 - Voltar")
        print("1 - Adicionar organizador")
        print("2 - Remover Organizador")

    def mostrar_menu_confirmar_participantes(self):
        print("------ Menu de Confirmação ------")
        print("Escolha sua opção:")
        print("0 - Voltar")
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
        print(i, evento.titulo)

    def mostrar_detalhes(self, evento):
        print("------ Visualizar evento ------")
        print("Nome: {}".format(evento.titulo))
        print("Data: {}".format(evento.data.strftime("%d/%m/%Y")))
        print("Horário: {}".format(evento.horario.strftime("%H:%M")))

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Evento ------") if not alterar else print(
            "------ Alterar Evento ------")

        evento = {}

        evento["titulo"] = self.ler_string(
            "Informe o título do evento: ", self.validar_string(min=3, max=50))

        evento["data"] = self.ler_data("Data do evento: ",
                                       self.validar_data(min=datetime.today()))

        evento["horario"] = self.ler_horario("Informe o horário do evento: ")

        evento["capacidade"] = self.ler_inteiro(
            "Informe a capacidade máxima do evento: ", self.validar_inteiro(min=1))

        evento["endereco"] = self.mostrar_tela_endereco()

        return evento

    def mostrar_registro(self, registro, i):
        print(i, registro.participante.nome)

    def mostrar_detalhes_registro(self, registro):
        print("------ Visualizar registro ------")
        print("Participante", registro.participante.nome)
        print("Entrada:", registro.entrada["data"], "-", registro.entrada["horario"])
        if(registro.saida):
            print("Saída:", registro.saida["data"], "-", registro.saida["horario"])

    def mostrar_tela_registrar_entrada(self, data_evento, horario_evento):

        print("------ Registrar entrada ------")

        while(True):
            data = self.ler_data("Informe a data da entrada.")

            if(data != data_evento):
                confirmacao = self.confirmar(
                    "A data informada não coincide com a data do evento. Deseja prosseguir mesmo assim? (s/n)")
                if(confirmacao):
                    break
            else:
                break

        while(True):
            horario = self.ler_horario("Informe o horário de entrada.")

            if(horario < horario_evento):
                confirmacao = self.confirmar(
                    "O horário informado é anterior ao do evento. Deseja prosseguir mesmo assim? (s/n)")
                if(confirmacao):
                    break
            else:
                break

        return {"data": data, "horario": horario}
