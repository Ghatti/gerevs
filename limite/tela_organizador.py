from limite.tela import Tela
from datetime import datetime, timedelta


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
            "Informe o nome do organizador: ", self.validar_string(min=4, max=31))
        organizador["cpf"] = self.ler_string(
            "Informe o cpf do organizador: ", self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"))
        organizador["nascimento"] = self.ler_data("Data de nascimento: ",
                                                  self.validar_data(max=datetime.today(), delta=timedelta(days=150*365)))
        organizador["endereco"] = self.mostrar_tela_endereco()
        return organizador
