from abc import ABC, abstractmethod
from limite.tela import Tela


class TelaIntegrante(Tela, ABC):

    @abstractmethod
    def __init__(self, controlador):

        super().__init__(controlador)

    def mostrar(self, pessoa, i):
        print(i, pessoa.nome)

    def mostrar_detalhes(self, pessoa):
        print("------ Visualização de Detalhes ------")
        print("Nome: {}".format(pessoa.nome))
        print("Cpf: {}".format(pessoa.cpf))
        print("Nascimento: {}".format(
            pessoa.nascimento.strftime("%d/%m/%Y")))
        self.mostrar_endereco(pessoa.endereco)
