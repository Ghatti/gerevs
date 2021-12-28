from abc import ABC, abstractmethod

class Controlador(ABC):

    @abstractmethod
    def __init__(self, controlador_sistema, tela):
        self.__controlador_sistema = controlador_sistema
        self.__tela = tela
        self.__entidades = []

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def entidades(self):
        return self.__entidades

    def abrir_menu_inicial(self):
        self.__tela.mostrar_menu_inicial()

    def abrir_menu_visualizacao(self):
        pass

    def abrir_tela_confirmacao(self):
        pass    

    def abrir_tela_mostrar(self):
        pass

    def abrir_tela_cadastro(self):
        pass

    def abrir_tela_detalhes(self):
        pass

    def abrir_tela_selecionar(self):
        pass  

    def ver_todos(self):
        pass

    def ver_detalhes(self):
        pass

    def listar(self):
        pass

    def mostrar(self, entidade):
        pass

    def selecionar(self):
        pass

    def cadastrar(self):
        pass

    def obter(self, id):
        pass

    def alterar(self, entidade):
        pass

    def remover(self, entidade):
        pass


