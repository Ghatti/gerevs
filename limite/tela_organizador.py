from limite.tela import Tela


class TelaOrganizador(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_menu_inicial(self):
        print("------ Modulo de Organizadores ------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Organizador")
        print("0 - Encerrar Sistema")

    def mostrar_tela_cadastro(self):
        print("------ Cadastrar Organizador ------")

        organizador = {}
        organizador["nome"] = self.ler_string(
            "Informe o nome do organizador: ", "O nome informado não é válido", self.validar_string(min=4, max=31))
        organizador["cpf"] = self.ler_string(
            "Informe o cpf do organizador: ", "O CPF informado não é válido. Utilize o formado 000.000.000-00", self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"))
        organizador["nascimento"] = self.ler_string("Informe a data de nascimento do organizador: ",
                                              "A data de nascimento informada não é válida. Utilize o formado 01/01/1900", self.validar_string(formato=r"^\d{2}\/\d{2}\/\d{4}$"))

        print("Agora, informe o endereço do organizador.")
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
        organizador["endereco"] = endereco.copy()
        return organizador