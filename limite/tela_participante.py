from limite.tela import Tela
from datetime import datetime, timedelta


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

    def mostrar_menu_visualizacao(self):
        print("------ Menu de Detalhes ------")
        print("Escolha sua opção:")
        print("1 - Alterar")
        print("2 - Remover")
        print("3 - Ver Cartão de Vacinas")
        print("4 - Ver Exame")
        print("0 - Voltar")

    def mostrar(self, participante, i):
        print(i, participante.nome)

    def mostrar_detalhes(self, participante):
        print("------ Visualizar Participante ------")
        print("Nome: {}".format(participante.nome))
        print("Cpf: {}".format(participante.cpf))
        print("Nascimento: {}".format(participante.nascimento))

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Participante ------") if not alterar else print(
            "------ Alterar Participante ------")

        participante = {}
        participante["nome"] = self.ler_string(
            "Informe o nome do participante: ", "O nome informado não é válido", self.validar_string(min=4, max=31))
        participante["cpf"] = self.ler_string(
            "Informe o cpf do participante: ", "O CPF informado não é válido. Utilize o formado 000.000.000-00", self.validar_string(formato=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"))
        participante["nascimento"] = self.ler_data("Data de nascimento: ",
                                                   "A data de nascimento informada não é válida. Utilize o formado 01/01/1900",
                                                   self.validar_data(max=datetime.today(), delta=timedelta(days=150*365)))
        participante["endereco"] = self.mostrar_tela_endereco()
        return participante

    def mostrar_tela_erro_exame(self):

        registrar = None
        while(registrar not in ["n", "s"]):
            registrar = self.ler_string(
                "Participante não possui exame cadastrado. Deseja registrar um exame? s/n", "A resposta informada não é válida. Responda sim (s) ou não (n).").strip().lower()

        return registrar == "s"
