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

    def mostrar(self, entidade):
        pass

    def mostrar_detalhes(self, entidade):
        pass

    def mostrar_menu_visualizacao(self):
        pass

    def confirmar(self):
        pass

    def selecionar(self):
        pass

    def mostrar_mensagem(self, mensagem):
        pass