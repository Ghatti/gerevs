from controle.controlador_organizador import ControladorOrganizador
from controle.controlador_participante import ControladorParticipante
from controle.controlador_evento import ControladorEvento
from controle.controlador_cartao_de_vacina import ControladorCartaoDeVacina
from controle.controlador_exame import ControladorExame
from controle.controlador_registro_de_presenca import ControladorRegistroDePresenca
from limite.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):

        self.__controlador_evento = ControladorEvento(self)
        self.__controlador_organizador = ControladorOrganizador(self)
        self.__controlador_participante = ControladorParticipante(self)
        self.__controlador_cartao_de_vacina = ControladorCartaoDeVacina(self)
        self.__controlador_exame = ControladorExame(self)
        self.__tela = TelaSistema(self)

    @property
    def controlador_evento(self):
        return self.__controlador_evento

    @property
    def controlador_organizador(self):
        return self.__controlador_organizador

    @property
    def controlador_participante(self):
        return self.__controlador_participante

    @property
    def controlador_cartao_de_vacina(self):
        return self.__controlador_cartao_de_vacina

    @property
    def controlador_exame(self):
        return self.__controlador_exame

    @property
    def tela(self):
        return self.__tela


    def inicializar(self):
        self.abrir_menu_inicial()

    def abrir_menu_inicial(self):

        opcoes = {1: self.iniciar_modulo_eventos, 2: self.iniciar_modulo_organizadores,
                  3: self.iniciar_modulo_participantes, 0: self.encerrar_sistema}

        while True:
            opcao_escolhida = self.tela.mostrar_menu_inicial()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()

    def iniciar_modulo_eventos(self):
        self.controlador_evento.inicializar()

    def iniciar_modulo_organizadores(self):
        self.controlador_organizador.inicializar()

    def iniciar_modulo_participantes(self):
        self.controlador_participante.inicializar()
        
    def encerrar_sistema(self):
        exit(0)
