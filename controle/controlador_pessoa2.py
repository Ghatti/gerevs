from controle.controlador import Controlador
from controle.controlador_organizador import ControladorOrganizador
from controle.controlador_participante import ControladorParticipante
from entidade.pessoa2 import Pessoa
from limite.tela import Tela


class ControladorPessoa(Controlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, Tela(self))
        self.__controlador_organizador = ControladorOrganizador(
            controlador_sistema, self)
        self.__controlador_participante = ControladorParticipante(
            controlador_sistema, self)

    @property
    def controlador_organizador(self):
        return self.__controlador_organizador

    @property
    def controlador_participante(self):
        return self.__controlador_participante

    def abrir_tela_cadastro(self):

        dados = self.tela.mostrar_tela_cadastro()

        for pessoa in self.entidades:
            if(pessoa.cpf == dados["cpf"]):
                raise ValueError(
                    "Já existe um cadastro com esse CPF.")

        return dados

    def cadastrar(self):
        try:

            dados = self.abrir_tela_cadastro()

        except ValueError as err:
            self.tela.mostrar_mensagem(err)
        else:

            # criar pessoa
            nova_pessoa = Pessoa(
                dados["cpf"], dados["nome"], dados["nascimento"], dados["endereco"])

            # incluir pessoa
            self.controlador_organizador.incluir(nova_pessoa)
