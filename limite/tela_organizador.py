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
        organizador["nome"] = self.ler_string("Informe o nome do organizador: ", "O nome informado não é válido", self.validar_string(min = 4, max = 31))
        #while True:
        #    try:
        #        organizador["nome"] = input("Informe o nome do organizador: ")
#
        #        if(len(organizador["nome"]) <= 5 or len(organizador["nome"]) >= 30):
        #            raise ValueError
        #        else:
        #            break
#
        #    except ValueError:
        #        print("O nome informado não é válido")

        while True:
            try:
                organizador.cpf = input("Informe o cpf do organizador: ")

                if(not re.match(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$", cpf)):
                    raise ValueError
                else:
                    break

            except ValueError:
                print("O CPF informado não é válido. Utilize o formado 000.000.000-00")

        while True:
            try:
                organizador.nasc = input(
                    "Informe a data de nascimento do organizador: ")

                if(not re.match(r"^\d{2}\/\d{2}\/\d{4}$", nasc)):
                    raise ValueError
                else:
                    break

            except ValueError:
                print(
                    "A data de nascimento informada não é válida. Utilize o formado 01/01/1900")

        print("Agora, informe o endereço do organizador.")

        endereco = {}

        while True:
            try:
                endereco.cep = input("CEP: ")

                if(not re.match(r"^\d{2}\.\d{3}\-\d{3}$", endereco.cep)):
                    raise ValueError
                else:
                    break

            except ValueError:
                print(
                    "O CEP informado não é válido. Utilize o formado 00.000-000")

        while True:
            try:
                endereco.rua = input("Rua: ")

                if(len(endereco.rua) == 0):
                    raise ValueError
                else:
                    break

            except ValueError:
                print("A rua informada não é válido")

        while True:
            try:
                endereco.rua = input("Rua: ")

                if(len(endereco.rua) == 0):
                    raise ValueError
                else:
                    break

            except ValueError:
                print("A rua informada não é válido")

        while True:
            try:
                endereco.numero = input("Numero: ")
                int(endereco.numero)
                break

            except ValueError:
                print("Por favor, informe um número")

        while True:
            try:
                endereco.bairro = input("Bairro: ")

                if(len(endereco.bairro) == 0):
                    raise ValueError
                else:
                    break

            except ValueError:
                print("O bairro informado não é válido")

        while True:
            try:
                endereco.cidade = input("Cidade: ")

                if(len(endereco.cidade) == 0):
                    raise ValueError
                else:
                    break

            except ValueError:
                print("A cidade informada não é válido")

        while True:
            try:
                endereco.estado = input("Estado: ")

                if(len(endereco.estado) == 0):
                    raise ValueError
                else:
                    break

            except ValueError:
                print("O estado informada não é válido")

        organizador.endereco = endereco.copy()


        