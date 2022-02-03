from limite.tela import Tela
from datetime import datetime, timedelta


class TelaExame(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Exame ------")

        exame = {}
        exame["data"] = self.ler_data("Informe a data do exame ",
                                      self.validar_data(max=datetime.today()))

        horario = self.ler_horario("Informe o horário da coleta: ")

        exame["data"] = exame["data"] + \
            timedelta(hours=horario.hour, minutes=horario.minute)

        exame["resultado"] = self.ler_string("Informe se o resultado foi positivo ou negativo: (p/n) ",
                                             self.validar_string(opcoes=["p", "n"])).strip().lower() == "p"

        return exame

    def mostrar_menu_visualizacao(self):
        print("------ Menu de Exame ------")
        print("Escolha sua opção:")
        print("1 - Registrar exame")
        print("0 - Voltar")

    def mostrar(self, exame, i):

        print(i, "-", exame.data.strftime("%d/%m/%Y - %H:%M"), "-",
              "Positivo" if exame.resultado else "Negativo")

