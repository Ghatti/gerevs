from entidade.organizador import Organizador
from controle.controlador_pessoa import ControladorPessoa
from limite.tela_organizador import TelaOrganizador


class ControladorOrganizador(ControladorPessoa):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaOrganizador(self))

    def cadastrar(self):

        try:
            dados = self.abrir_tela_cadastro()

        except ValueError as err:
            self.tela.mostrar_mensagem(err)
        else:

            # criar organizador
            novo_organizador = Organizador(
                dados["cpf"], dados["nome"], dados["nascimento"], dados["endereco"])

            # incluir organizador
            self.entidades.append(novo_organizador)
            self.tela.mostrar_mensagem("Organizador cadastrado com sucesso")
            self.ver_todos()
