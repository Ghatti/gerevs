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

    @property
    def tela(self):
        return self.__tela

    def inicializar(self):
        self.abrir_menu_inicial()

    @abstractmethod
    def abrir_menu_inicial(self):
        pass

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
        print("Cadastrar selecionado")

    def obter(self, id):
        pass

    def alterar(self, entidade):
        pass

    def remover(self, entidade):
        pass

    def abrir_menu(self, menu=None, opcoes={}, opcoes_validas=[]):

        while True:
            menu()
            opcao_escolhida = self.tela.ler_inteiro(opcoes_validas)
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()
