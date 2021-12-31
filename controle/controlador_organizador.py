from entidade.organizador import Organizador
from entidade.endereco import Endereco
from controle.controlador import Controlador
from limite.tela_organizador import TelaOrganizador


class ControladorOrganizador(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaOrganizador(self))

    def ver_eventos(self, organizador):
        pass

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar}
        opcoes_validas = [0, 1]
        menu = self.tela.mostrar_menu_inicial

        while(True):
            self.listar()
            self.abrir_menu(menu, opcoes, opcoes_validas)

    def cadastrar(self):

        dados = self.tela.mostrar_tela_cadastro()

        try:
            # Procurar se há organizador com o cpf
            for organizador in self.entidades:
                if(organizador.cpf == dados["cpf"]):
                    raise ValueError
        except ValueError:
            self.tela.mostrar_mensagem(
                "Erro: Já existe um organizador cadastrado com esse CPF.")
        else:

            # criar organizador
            novo_organizador = Organizador(
                dados["cpf"], dados["nome"], dados["nascimento"], dados["endereco"])

            # incluir organizador
            self.entidades.append(novo_organizador)
            self.tela.mostrar_mensagem("Organizador cadastrado com sucesso")
