from controle.controlador import Controlador
from controle.controlador_organizador import ControladorOrganizador
from controle.controlador_participante import ControladorParticipante
from entidade.pessoa import Pessoa
from limite.tela_pessoa import TelaPessoa
from dao.pessoa_dao import PessoaDAO


class ControladorPessoa(Controlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaPessoa(self), PessoaDAO("pessoas.pkl"))
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

    def cadastrar(self, incluir):

        # abre a tela de cadastro
        # obtem cpf
        # Se cpf já cadastrado, retorna a pessoa cadastrada. Verificar se está na lista. Senão, inclui.
        # Se cpf não cadastrado, segue o jogo.

        try:

            dados = self.abrir_tela_cadastro()

            if dados is None:
                return

            for pessoa in self.entidades:
                if(pessoa.cpf == dados["cpf"]):

                    prosseguir = self.tela.mostrar_tela_cadastro_repetido(
                        self.unpack(pessoa))
                    if(prosseguir):
                        incluir(pessoa)
                        return
                    else:
                        raise ValueError(
                            "Não é possível cadastrar duas pessoas com o mesmo CPF.")

        except ValueError as err:
            self.tela.mostrar_mensagem(err, "Erro")
        else:

            endereco = {
                "cep": dados["cep"],
                "rua": dados["rua"],
                "numero": dados["numero"],
                "bairro": dados["bairro"],
                "cidade": dados["cidade"],
                "estado": dados["estado"],
            }

            # criar pessoa
            nova_pessoa = Pessoa(
                dados["cpf"], dados["nome"], dados["nascimento"], endereco)

            # incluir pessoa
            self.dao.persist(nova_pessoa)
            incluir(nova_pessoa)

    def alterar(self, dados):

        try:
            entidade = self.get_entidade(dados["row_index"])

            dados = self.tela.mostrar_tela_cadastro(
                default_values=self.unpack(entidade), alterar=True)

            novo_endereco = {
                "cep": dados["cep"],
                "rua": dados["rua"],
                "numero": dados["numero"],
                "bairro": dados["bairro"],
                "cidade": dados["cidade"],
                "estado": dados["estado"]
            }

            entidade.nome = dados["nome"]
            entidade.nascimento = dados["nascimento"]
            entidade.endereco = novo_endereco

            self.dao.persist(entidade)
        except ValueError as err:
            self.tela.mostrar_mensagem("Erro", err)

    def unpack(self, pessoa):

        return {
            "nome": pessoa.nome,
            "cpf": pessoa.cpf,
            "nascimento": pessoa.nascimento.strftime("%d/%m/%Y"),
            "cep": pessoa.endereco.cep,
            "rua": pessoa.endereco.rua,
            "numero": pessoa.endereco.numero,
            "bairro": pessoa.endereco.bairro,
            "cidade": pessoa.endereco.cidade,
            "estado": pessoa.endereco.estado,
        }
