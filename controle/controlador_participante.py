from controle.controlador_integrante import ControladorIntegrante
from limite.tela_participante import TelaParticipante


class ControladorParticipante(ControladorIntegrante):

    def __init__(self, controlador_sistema, controlador_pessoa):
        super().__init__(controlador_sistema, controlador_pessoa, TelaParticipante(self))

    def abrir_menu_visualizacao(self, participante):

        opcoes = {1: lambda participante: self.controlador_sistema.controlador_cartao_de_vacina.registrar_dose(
            participante.cartao_de_vacina), 2: self.mostrar_exames}

        def menu():
            return self.tela.mostrar_detalhes(self.unpack(participante))

        self.abrir_menu(menu, opcoes,  participante)

    def registrar_exame(self, participante):

        novo_exame = self.controlador_sistema.controlador_exame.cadastrar()

        if(participante.nascimento > novo_exame.data):
            raise ValueError(
                "O exame não pode ser realizado antes do nascimento do participante.")

        participante.add_exame(novo_exame)
        self.controlador_sistema.controlador_exame.listar(
            participante.exames)

    def mostrar_exames(self, participante):

        self.controlador_sistema.controlador_exame.mostrar(
            participante.exames, lambda: self.registrar_exame(participante))
