from limite.tela import Tela


class TelaExame(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Exame ------")

        exame = {}
        exame["data"] = self.ler_string("Informe a data do exame: ",
                                        "A data informada não é válida. Utilize o formado 01/01/1900", self.validar_string(formato=r"^\d{2}\/\d{2}\/\d{4}$"))

        resultado = self.ler_string("Informe se o resultado foi positivo ou negativo: (p/n) ",
                                    "O valor informado não é válido, informe p para positivo ou n para negativo").strip().lower()

        exame["resultado"] = resultado == "p"

        return exame

    def mostrar_menu_visualizacao(self):
        print("------ Menu de Exame ------")
        print("Escolha sua opção:")
        print("1 - Registrar exame")
        print("0 - Voltar")

    def mostrar_detalhes(self, exame):
        print("------ Cadastrar Cartão de Vacina ------")
        print("Data: {}".format(exame.data))
        print("Resultado: {}".format(
            "Positivo" if exame.resultado else "Negativo"))
