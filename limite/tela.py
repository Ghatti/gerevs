import re
from abc import ABC, abstractmethod


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
        print("0 - Encerrar Sistema")

    def confirmar(self):
        pass

    def selecionar(self):
        pass

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

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

    def ler_string(self, input_msg, err_msg, validators = []):

        while True:
            try:
                valor_informado = input(input_msg)

                for validator in validators:
                    if(not validator(valor_informado)):
                        raise ValueError
                
                return valor_informado

            except ValueError:
                print(err_msg)


    def validar_string(self, min = None, max = None, equal = None, formato = None):

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
