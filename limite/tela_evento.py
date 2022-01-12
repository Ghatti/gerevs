from limite.tela import Tela


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

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Evento ------") if not alterar else print(
            "------ Alterar Evento ------")

        evento = {}

        evento["titulo"] = self.ler_string(
            "Informe o título do evento: ", "O título informado não é válido.", self.validar_string(min=3, max=50))

        # add validation for data. Allow only future eventos.
        evento["data"] = self.ler_string(
            "Informe a data do evento: ", "A data informada não é válida. Utilize o formato 01/01/1990", self.validar_string(formato=r"^\d{2}\/\d{2}\/\d{4}$"))

        # verify format of horario
        evento["horario"] = self.ler_string(
            "Informe o horário do evento: ", "O horário informado não é válido. Utilize o formato hh:mm", self.validar_string(formato=r"^\d{2}\:\d{2}$"))

        # add validation for capacidade
        while True:
            try:
                evento["capacidade"] = input(
                    "Informe a capacidade do evento: ")
                int(evento["capacidade"])
                break

            except ValueError:
                print()

        # implement selection of organizador
        # evento["organizador"] =

        print("Agora, informe o endereço do evento.")
        evento["endereco"] = self.mostrar_tela_endereco()

        return evento
