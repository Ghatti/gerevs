from controle.controlador import Controlador
from controle.controlador_organizador import ControladorOrganizador
from controle.controlador_participante import ControladorParticipante
from entidade.pessoa import Pessoa
from limite.tela_pessoa import TelaPessoa


class ControladorPessoa(Controlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaPessoa(self))
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

        return dados

    def cadastrar(self, incluir):

        # abre a tela de cadastro
        # obtem cpf
        # Se cpf já cadastrado, retorna a pessoa cadastrada. Verificar se está na lista. Senão, inclui.
        # Se cpf não cadastrado, segue o jogo.

        try:

            cpf = self.tela.ler_cpf()

            for pessoa in self.entidades:
                if(pessoa.cpf == cpf):

                    prosseguir = self.tela.mostrar_tela_cadastro_repetido(
                        pessoa)

                    if(prosseguir):
                        incluir(pessoa)
                        return
                    else:
                        raise ValueError(
                            "Não é possível cadastrar duas pessoas com o mesmo CPF.")

            dados = self.abrir_tela_cadastro()

        except ValueError as err:
            self.tela.mostrar_mensagem(err)
        else:

            # criar pessoa
            nova_pessoa = Pessoa(
                cpf, dados["nome"], dados["nascimento"], dados["endereco"])

            # incluir pessoa
            self.entidades.append(nova_pessoa)
            incluir(nova_pessoa)

    def alterar(self, pessoa):

        dados = self.tela.mostrar_tela_cadastro(alterar=True)

        pessoa.nome = dados["nome"]
        pessoa.nascimento = dados["nascimento"]
        pessoa.endereco = dados["endereco"]

        self.tela.mostrar_detalhes(pessoa)
