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

    def mostrar(self, evento, i):
        print(i, evento.titulo)

    def mostrar_detalhes(self, evento):
        print("------ Visualizar evento ------")
        print("Nome: {}".format(evento.titulo))
        print("Data: {}".format(evento.data))
        print("Horário: {}".format(evento.horario))

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Evento ------") if not alterar else print(
            "------ Alterar Evento ------")

        evento = {}

        evento["titulo"] = self.ler_string(
            "Informe o título do evento: ", "O título informado não é válido.", self.validar_string(min=3, max=50))

        # add validation for data. Allow only future eventos.
        evento["data"] = self.ler_data("Data do evento: ",
                                       "A data informada não é válida. Utilize o formado 01/01/1900",
                                       self.validar_data(min=datetime.today()))

        # verify format of horario
        evento["horario"] = time.fromisoformat(self.ler_string(
            "Informe o horário do evento: ", "O horário informado não é válido. Utilize o formato hh:mm", self.validar_string(formato=r"^\d{2}\:\d{2}$")))

        # add validation for capacidade
        while True:
            try:
                evento["capacidade"] = input(
                    "Informe a capacidade do evento: ")
                int(evento["capacidade"])
                break

            except ValueError:
                print()

        evento["endereco"] = self.mostrar_tela_endereco()

        return evento
