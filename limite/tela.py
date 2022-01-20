import re
from abc import ABC, abstractmethod
from datetime import datetime


class Tela(ABC):

    @abstractmethod
    def __init__(self, controlador):
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador

    def mostrar_menu_inicial(self):
        pass

    def mostrar_tela_cadastro(self):
        pass

    def mostrar(self, entidade, i):
        pass

    def mostrar_detalhes(self, entidade):
        pass

    def mostrar_menu_visualizacao(self):
        print("------ Menu de Detalhes ------")
        print("Escolha sua opção:")
        print("1 - Alterar")
        print("2 - Remover")
        print("0 - Voltar")

    def confirmar(self):
        confirmacao = "t"
        while(confirmacao not in ["n", "s"]):
            confirmacao = input("Deseja confirmar a operação? s/n").lower()
        return confirmacao == "s"

    def selecionar(self):
        pass

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_tela_endereco(self):
        print("Agora, informe o endereço.")
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

        return endereco

    def ler_inteiro(self, opcoes=[]):

        while True:
            opcao = input("Escolha a opcao:")

            try:
                opcao = int(opcao)
                if(opcao not in opcoes):
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor incorreto. Digite um valor numérico válido.")

    def ler_string(self, input_msg, err_msg, validators=[]):

        while True:
            try:
                valor_informado = input(input_msg)

                for validator in validators:
                    if(not validator(valor_informado)):
                        raise ValueError

                return valor_informado

            except ValueError:
                print(err_msg)

    def ler_data(self, input_msg, err_msg, validators=[]):

        while True:

            date_string = self.ler_string(
                input_msg, err_msg, self.validar_string(formato=r"^\d{2}\/\d{2}\/\d{4}$"))

            try:
                date = datetime.strptime(date_string, "%d/%m/%Y")

                for validator in validators:
                    if(not validator(date)):
                        raise ValueError

                return date

            except ValueError:
                print("Data inválida")

    def validar_string(self, min=None, max=None, equal=None, formato=None):

        validators = []

        if(min):
            def validar_minimo(valor):
                return len(valor) > min
            validators.append(validar_minimo)

        if(max):
            def validar_maximo(valor):
                return len(valor) < max
            validators.append(validar_maximo)

        if(equal):
            def validar_not_igual(valor):
                return not len(valor) == equal
            validators.append(validar_not_igual)

        if(formato):
            def validar_formato(valor):
                return re.match(formato, valor)
            validators.append(validar_formato)

        return validators

    def validar_data(self, min=None, max=None, delta=None):

        validators = []
        if(min):
            def validar_minimo(valor):
                return valor > min
            validators.append(validar_minimo)

        if(max):
            def validar_maximo(valor):
                return valor < max
            validators.append(validar_maximo)

        if(delta):
            def validar_delta(valor):
                return datetime.today() - valor < delta
            validators.append(validar_delta)

        return validators
