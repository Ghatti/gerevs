from limite.tela import Tela


class TelaOrganizador(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_menu_inicial(self):
        print("------ Modulo de Organizadores ------")
        print("Escolha sua opção:")
        print("1 - Cadastrar Organizador")
        print("2 - Listar Organizadores")
        print("3 - Ver Organizador")
        print("0 - Voltar")

    def mostrar(self, organizador, i):
        print(i, organizador.nome)

    def mostrar_detalhes(self, organizador):
        print("------ Visualizar Organizador ------")
        print("Nome: {}".format(organizador.nome))
        print("Cpf: {}".format(organizador.cpf))
        print("Nascimento: {}".format(organizador.nascimento))

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Organizador ------") if not alterar else print(
            "------ Alterar Organizador ------")

        organizador = {}
        organizador["nome"] = self.ler_string(
            "Informe o nome do organizador: ", "O nome informado não é válido", self.validar_string(min=4, max=31))
        organizador["cpf"] = self.ler_string(
            "Informe o cpf do organizador: ", "O CPF informado não é válido. Utilize o formado 000.000.000-00", self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"))
        organizador["nascimento"] = self.ler_string("Informe a data de nascimento do organizador: ",
                                                    "A data de nascimento informada não é válida. Utilize o formado 01/01/1900", self.validar_string(formato=r"^\d{2}\/\d{2}\/\d{4}$"))
        organizador["endereco"] = self.mostrar_tela_endereco()
        return organizador
