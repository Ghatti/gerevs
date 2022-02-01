from limite.tela import Tela
from datetime import datetime, timedelta


class TelaPessoa(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def ler_cpf(self):
        return self.ler_string(
            "Informe o cpf: ", self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"))

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar ------") if not alterar else print(
            "------ Alterar ------")

        pessoa = {}
        pessoa["nome"] = self.ler_string(
            "Informe o nome: ", self.validar_string(min=4, max=31, no_digit=True))
        pessoa["nascimento"] = self.ler_data("Data de nascimento: ",
                                             self.validar_data(max=datetime.today(), delta=timedelta(days=150*365)))
        pessoa["endereco"] = self.mostrar_tela_endereco()
        return pessoa

    def mostrar_tela_cadastro_repetido(self, pessoa):
        self.mostrar_mensagem(
            "Já existe uma pessoa cadastrada com esse CPF")
        self.mostrar_detalhes(pessoa)
        return self.ler_string(
            "Deseja prosseguir com essa pessoa? (s/n)", self.validar_string(opcoes=("s", "n"))) == "s"

    def mostrar(self, pessoa, i):
        print(i, pessoa.nome)

    def mostrar_detalhes(self, pessoa):
        print("------ Visualização de Detalhes ------")
        print("Nome: {}".format(pessoa.nome))
        print("Cpf: {}".format(pessoa.cpf))
        print("Nascimento: {}".format(
            pessoa.nascimento.strftime("%d/%m/%Y")))
