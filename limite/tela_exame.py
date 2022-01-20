from limite.tela import Tela


class TelaExame(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

    def mostrar_tela_cadastro(self, alterar=False):
        print("------ Cadastrar Exame ------")

        exame = {}
        exame["data"] = self.ler_data("Informe a data do exame ",
                                      "A data não é válida. Utilize o formado 01/01/1900")

        resultado = None
        while(resultado not in ["p", "n"]):
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
        print("------ Visualização de Exame ------")
        print("Data: {}".format(exame.data))
        print("Resultado: {}".format(
            "Positivo" if exame.resultado else "Negativo"))
