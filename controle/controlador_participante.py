from controle.controlador_integrante import ControladorIntegrante
from limite.tela_participante import TelaParticipante
from dao.participante_dao import ParticipanteDAO
from exceptions.cancelOperationException import CancelOperationException


class ControladorParticipante(ControladorIntegrante):

    def __init__(self, controlador_sistema, controlador_pessoa):
        super().__init__(controlador_sistema, controlador_pessoa,
                         TelaParticipante(self), ParticipanteDAO())

    def abrir_menu_visualizacao(self, participante):

        opcoes = {1: self.registrar_vacina, 2: self.mostrar_exames}

        def menu():
            return self.tela.mostrar_detalhes(self.unpack(participante))

        self.abrir_menu(menu, opcoes,  participante)

    def registrar_vacina(self, participante):
        self.controlador_sistema.controlador_cartao_de_vacina.registrar_dose(
            participante.cartao_de_vacina)
        self.persist_change(participante)

    def registrar_exame(self, participante):

        try:
            novo_exame = self.controlador_sistema.controlador_exame.cadastrar()

            if novo_exame is None:
                return

            if(participante.nascimento > novo_exame.data):
                raise ValueError(
                    "O exame não pode ser realizado antes do nascimento do participante.")

            participante.add_exame(novo_exame)
            self.persist_change(participante)
        except CancelOperationException as err:
            self.tela.mostrar_mensagem(err, "Operação cancelada")

    def mostrar_exames(self, participante):

        self.controlador_sistema.controlador_exame.mostrar(
            participante.exames, lambda: self.registrar_exame(participante))

    def persist_change(self, participante):
        self.dao.persist(participante)
        self.controlador_sistema.controlador_evento.atualizar_pessoa(
            participante)
