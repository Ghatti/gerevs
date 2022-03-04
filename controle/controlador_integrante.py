from controle.controlador import Controlador


class ControladorIntegrante(Controlador):

    def __init__(self, controlador_sistema, controlador_pessoa, tela):
        super().__init__(controlador_sistema, tela)
        self.__controlador_pessoa = controlador_pessoa

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

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

    def unpack(self, pessoa):

        return pessoa.nome
