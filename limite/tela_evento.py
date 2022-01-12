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

        #self.__titulo = titulo
        #self.__data = data
        #self.__horario = horario
        #self.__local = local
        #self.__capacidade = capacidade
        #self.__organizadores = [organizador]

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
                evento["capacidade"] = input("Informe a capacidade do evento: ")
                int(evento["capacidade"])
                break

            except ValueError:
                print()

        #implement selection of organizador
        #evento["organizador"] =

        print("Agora, informe o endereço do evento.")
        endereco = {}

        endereco["cep"] = self.ler_string(
            "CEP: ", "O CEP informado não é válido. Utilize o formado 00.000-000", self.validar_string(formato=r"^\d{2}\.\d{3}\-\d{3}$"))
        endereco["rua"] = self.ler_string(
            "Rua: ", "A rua informada não é válido", self.validar_string(equal=0))

        # probably make a function to validate int later
        while True:
            try:
                endereco["numero"] = input("Informe o número: ")
                int(endereco["numero"])
                break

            except ValueError:
                print()

        endereco["bairro"] = self.ler_string(
            "Bairro: ", "O bairro informado não é válido", self.validar_string(
                equal=0)
        )
        endereco["cidade"] = self.ler_string(
            "Cidade: ", "A cidade informada não é válida", self.validar_string(
                equal=0)
        )
        endereco["estado"] = self.ler_string(
            "Estado: ", "O estado informado não é válido", self.validar_string(
                equal=0)
        )        

        evento["endereco"] = endereco.copy()
        return evento