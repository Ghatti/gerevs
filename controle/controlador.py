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

        opcoes = {1: lambda input: self.cadastrar(
        ), 2: lambda input: self.alterar(input), 3: lambda input: self.ver_detalhes(input), 4: lambda input: self.remover(input)}

        def menu():
            entidades = [self.unpack(entidade) for entidade in self.entidades]
            return self.tela.mostrar_menu_inicial(entidades)

        self.abrir_menu(menu, opcoes)

    def abrir_menu_visualizacao(self, entidade):

        opcoes = {}

        def menu():
            self.tela.mostrar_detalhes(self.unpack(entidade))
            return 0, None

        self.abrir_menu(menu, opcoes, entidade)

    def abrir_tela_cadastro(self):

        dados = self.tela.mostrar_tela_cadastro()

        return dados

    def abrir_tela_selecionar(self, lista):
        return self.tela.selecionar(self.unpack_all(lista))

    def tem_entidades(self):
        return len(self.entidades) != 0

    def ver_todos(self):
        try:
            self.listar(self.entidades)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def get_entidade(self, index):

        if(len(index) == 0):
            raise ValueError("É necessário selecionar um item.")

        id = index[0]
        entidade = self.entidades[id]
        return entidade

    def ver_detalhes(self, dados):

        try:
            entidade = self.get_entidade(dados["row_index"])
            self.abrir_menu_visualizacao(entidade)

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def listar(self, lista=[]):

        if(len(lista) == 0):
            raise ValueError("Não há elementos para listar")
        for i, entidade in enumerate(lista):
            self.tela.mostrar(self.unpack(entidade))

    def selecionar(self, lista=None):

        if lista is None:
            lista = self.entidades

        opcao = self.abrir_tela_selecionar(lista)

        if(opcao is None):
            return None

        entidade = lista[opcao]
        return entidade

    # @abstract
    def cadastrar(self):
        pass

    # @abstract
    def alterar(self, entidade):
        pass

    def remover(self, dados):

        try:
            confirmacao = self.tela.confirmar()
            if(confirmacao):
                entidade = self.get_entidade(dados["row_index"])
                self.entidades.remove(entidade)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def abrir_menu(self, menu=None, opcoes={}, entidade=None):

        try:
            while(True):
                opcao_escolhida, dados = menu()

                if(opcao_escolhida == 0):
                    break

                funcao_escolhida = opcoes[opcao_escolhida]
                funcao_escolhida(
                    entidade) if entidade else funcao_escolhida(dados)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)
        except StopIteration as err:
            return

    def unpack_all(self, lista):

        return [self.unpack(item) for item in lista]

    def unpack(self, entidade):
        pass
