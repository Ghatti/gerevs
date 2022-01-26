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

    def abrir_menu_inicial(self):
        pass

    def abrir_menu_visualizacao(self, entidade):

        opcoes = {1: self.alterar, 2: self.remover}
        opcoes_validas = [0, 1, 2]
        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes, opcoes_validas, entidade)

    def abrir_tela_confirmacao(self):
        pass

    def abrir_tela_mostrar(self):
        pass

    def abrir_tela_cadastro(self):
        pass

    def abrir_tela_detalhes(self):
        pass

    def abrir_tela_selecionar(self):
        return self.tela.selecionar(range(1, len(self.entidades)+1))

    def tem_entidades(self):
        return len(self.entidades) != 0

    def ver_todos(self):
        self.listar(self.entidades)

    def ver_detalhes(self):

        if(len(self.entidades) == 0):
            self.tela.mostrar_mensagem("Ainda não foram realizados cadastros")
        else:

            entidade = self.selecionar(listar=True)
            self.tela.mostrar_detalhes(entidade)
            self.abrir_menu_visualizacao(entidade)

    def listar(self, lista=[]):

        if(len(lista) == 0):
            self.tela.mostrar_mensagem(
                "Não há elementos para listar")
        else:
            self.tela.mostrar_mensagem("------ Lista ------")
            for i, entidade in enumerate(lista):
                self.tela.mostrar(entidade, i+1)

    def mostrar(self, entidade):
        pass

    def selecionar(self, listar=False, lista=None):

        if lista is None:
            lista = self.entidades
    
        if(listar):
            self.listar(lista)

        opcao = self.abrir_tela_selecionar()
        entidade = lista[opcao-1]

        return entidade

    def cadastrar(self):
        pass

    def obter(self, id):
        pass

    def alterar(self, entidade):
        pass

    def remover(self, entidade):
        pass

    def abrir_menu(self, menu=None, opcoes={}, opcoes_validas=[], entidade=None):

        while(True):
            menu()
            opcao_escolhida = self.tela.selecionar(opcoes_validas)

            if(opcao_escolhida == 0):
                break

            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida(entidade) if entidade else funcao_escolhida()
