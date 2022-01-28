from abc import ABC, abstractmethod
from controle.controlador import Controlador


class ControladorPessoa(Controlador, ABC):

    def __init__(self, controlador_sistema, tela):
        super().__init__(controlador_sistema, tela)

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar, 2: self.ver_todos, 3: self.ver_detalhes}
        opcoes_validas = [0, 1, 2, 3]
        menu = self.tela.mostrar_menu_inicial

        self.ver_todos()
        self.abrir_menu(menu, opcoes, opcoes_validas)

    @abstractmethod
    def cadastrar(self):
        pass

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