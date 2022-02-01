from abc import ABC, abstractmethod
from multiprocessing.sharedctypes import Value
from controle.controlador import Controlador


class ControladorIntegrante(Controlador, ABC):

    def __init__(self, controlador_sistema, controlador_pessoa, tela):
        super().__init__(controlador_sistema, tela)
        self.__controlador_pessoa = controlador_pessoa

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar, 2: self.ver_todos, 3: self.ver_detalhes}

        menu = self.tela.mostrar_menu_inicial

        self.ver_todos()
        self.abrir_menu(menu, opcoes)

    def cadastrar(self):

        self.controlador_pessoa.cadastrar(self.incluir)

    def incluir(self, pessoa):
        if(pessoa in self.entidades):
            raise ValueError("A pessoa indicada já está cadastrada!")

        self.entidades.append(pessoa)
        self.tela.mostrar_mensagem("Cadastro realizado com sucesso")
        self.ver_todos()

    def alterar(self, pessoa):

        self.controlador_pessoa.alterar(pessoa)
