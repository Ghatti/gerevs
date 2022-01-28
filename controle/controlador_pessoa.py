from abc import ABC, abstractmethod
from controle.controlador import Controlador


class ControladorPessoa(Controlador, ABC):

    def __init__(self, controlador_sistema, tela):
        super().__init__(controlador_sistema, tela)

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar, 2: self.ver_todos, 3: self.ver_detalhes}

        menu = self.tela.mostrar_menu_inicial

        self.ver_todos()
        self.abrir_menu(menu, opcoes)

    @abstractmethod
    def cadastrar(self):
        pass

    def abrir_tela_cadastro(self):

        dados = self.tela.mostrar_tela_cadastro()

        for pessoa in self.entidades:
            if(pessoa.cpf == dados["cpf"]):
                raise ValueError(
                    "Já existe um cadastro com esse CPF.")

        return dados


    def alterar(self, pessoa):

        dados = self.tela.mostrar_tela_cadastro(alterar=True)

        pessoa.nome = dados["nome"]
        pessoa.cpf = dados["cpf"]
        pessoa.nascimento = dados["nascimento"]
        pessoa.endereco = dados["endereco"]

        self.tela.mostrar_detalhes(pessoa)

    def remover(self, pessoa):
        # first version
        # Later, add verification for events that have the organizador listed

        confirmacao = self.tela.confirmar()
        if(confirmacao):
            self.entidades.remove(pessoa)
