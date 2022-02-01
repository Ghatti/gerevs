from abc import ABC, abstractmethod
from limite.tela import Tela
from datetime import datetime, timedelta


class TelaPessoa(Tela, ABC):

    @abstractmethod
    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar_menu_inicial(self):
        print("------ Menu Inicial ------")
        print("Escolha sua opção:")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Ver Detalhes")
        print("0 - Voltar")

    def mostrar(self, pessoa, i):
        print(i, pessoa.nome)

    def mostrar_detalhes(self, pessoa):
        print("------ Visualização de Detalhes ------")
        print("Nome: {}".format(pessoa.nome))
        print("Cpf: {}".format(pessoa.cpf))
        print("Nascimento: {}".format(
            pessoa.nascimento.strftime("%d/%m/%Y")))

