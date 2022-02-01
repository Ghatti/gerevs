from limite.tela import Tela
from datetime import datetime, timedelta


class TelaPessoa(Tela):

    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar ------") if not alterar else print(
            "------ Alterar ------")

        pessoa = {}
        pessoa["nome"] = self.ler_string(
            "Informe o nome: ", self.validar_string(min=4, max=31, no_digit=True))
        pessoa["cpf"] = self.ler_string(
            "Informe o cpf: ", self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"))
        pessoa["nascimento"] = self.ler_data("Data de nascimento: ",
                                             self.validar_data(max=datetime.today(), delta=timedelta(days=150*365)))
        pessoa["endereco"] = self.mostrar_tela_endereco()
        return pessoa
