from entidade.organizador import Organizador
from controle.controlador_pessoa import ControladorPessoa
from limite.tela_organizador import TelaOrganizador


class ControladorOrganizador(ControladorPessoa):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaOrganizador(self))


    def cadastrar(self):

        dados = self.tela.mostrar_tela_cadastro()

        try:
            for organizador in self.entidades:
                if(organizador.cpf == dados["cpf"]):
                    raise ValueError(
                        "Já existe um organizador cadastrado com esse CPF")
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



