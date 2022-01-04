from limite.tela import Tela


class TelaParticipante(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_menu_inicial(self):
        print("------ Modulo de Participantes ------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Participante")
        print("2 - Listar Participantes")
        print("3 - Ver Participante")
        print("0 - Voltar")

    def mostrar(self, participante, i):
        print(i, participante.nome)

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Participante ------") if not alterar else print(
            "------ Alterar Participante ------")

        participante = {}
        participante["nome"] = self.ler_string(
            "Informe o nome do participante: ", "O nome informado não é válido", self.validar_string(min=4, max=31))
        participante["cpf"] = self.ler_string(
            "Informe o cpf do participante: ", "O CPF informado não é válido. Utilize o formado 000.000.000-00", self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"))
        participante["nascimento"] = self.ler_string("Informe a data de nascimento do participante: ",
                                                    "A data de nascimento informada não é válida. Utilize o formado 01/01/1900", self.validar_string(formato=r"^\d{2}\/\d{2}\/\d{4}$"))

        print("Agora, informe o endereço do participante.")
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
        participante["endereco"] = endereco.copy()
        return participante

