from entidade.participante import Participante
from controle.controlador_integrante import ControladorIntegrante
from limite.tela_participante import TelaParticipante


class ControladorParticipante(ControladorIntegrante):

    def __init__(self, controlador_sistema, controlador_pessoa):
        super().__init__(controlador_sistema, controlador_pessoa, TelaParticipante(self))

    def abrir_menu_visualizacao(self, participante):

        opcoes = {1: self.alterar, 2: self.remover,
                  3: self.mostrar_vacinas, 4: self.mostrar_exame}

        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes,  participante)

    def mostrar_vacinas(self, participante):

        cartao = participante.cartao_de_vacina

        self.controlador_sistema.controlador_cartao_de_vacina.mostrar(cartao)

    def registrar_exame(self, participante):

        participante.exame = self.controlador_sistema.controlador_exame.cadastrar()

    def mostrar_exame(self, participante):
        # the lambda function is a workaround for now. Not liking this solution.
        try:
            self.controlador_sistema.controlador_exame.mostrar(
                participante.exame, lambda: self.registrar_exame(participante))
        except AttributeError as err:
            print(err)
            registrar = self.tela.mostrar_tela_erro_exame()
            if(registrar):
                self.registrar_exame(participante)

    # def cadastrar(self):
#
    #   try:
#
    #       dados = self.abrir_tela_cadastro()
    #       cartao_de_vacina = self.controlador_sistema.controlador_cartao_de_vacina.cadastrar()
#
    #   except ValueError as err:
    #       self.tela.mostrar_mensagem(err)
    #   else:
#
    #       # criar participante
    #       novo_participante = Participante(
    #           dados["cpf"], dados["nome"], dados["nascimento"], dados["endereco"], cartao_de_vacina)
#
    #       # incluir participante
    #       self.entidades.append(novo_participante)
    #       self.tela.mostrar_mensagem("Participante cadastrado com sucesso")
    #       self.ver_todos()
