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

        opcoes = {1: self.cadastrar, 2: self.ver_todos, 3: self.ver_detalhes}

        menu = self.tela.mostrar_menu_inicial

        self.ver_todos()
        self.abrir_menu(menu, opcoes)

    def abrir_menu_visualizacao(self, entidade):

        opcoes = {1: self.alterar, 2: self.remover}

        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes, entidade)

    def abrir_tela_cadastro(self):

        dados = self.tela.mostrar_tela_cadastro()

        return dados

    def abrir_tela_selecionar(self, lista):
        return self.tela.selecionar(range(1, len(lista)+1))

    def tem_entidades(self):
        return len(self.entidades) != 0

    def ver_todos(self):
        try:
            self.listar(self.entidades)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def ver_detalhes(self):

        try:
            entidade = self.selecionar(self.entidades)
            self.tela.mostrar_detalhes(entidade)
            self.abrir_menu_visualizacao(entidade)

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def listar(self, lista=[]):

        if(len(lista) == 0):
            raise ValueError("Não há elementos para listar")
        self.tela.mostrar_mensagem("------ Lista ------")
        for i, entidade in enumerate(lista):
            self.tela.mostrar(entidade, i+1)

    def mostrar(self, entidade):
        pass

    def selecionar(self, lista=None, listar=True):

        if lista is None:
            lista = self.entidades

        if(listar):
            self.listar(lista)

        opcao = self.abrir_tela_selecionar(lista)
        entidade = lista[opcao-1]
        return entidade

    # @abstract
    def cadastrar(self):
        pass

    # @abstract
    def alterar(self, entidade):
        pass

    def remover(self, entidade):

        confirmacao = self.tela.confirmar()
        if(confirmacao):
            self.entidades.remove(entidade)
            raise StopIteration

    def abrir_menu(self, menu=None, opcoes={}, entidade=None):

        try:
            while(True):
                menu()
                opcao_escolhida = self.tela.selecionar(range(0, len(opcoes)+1))

                if(opcao_escolhida == 0):
                    break

                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida(entidade) if entidade else funcao_escolhida()
        except StopIteration:
            return
