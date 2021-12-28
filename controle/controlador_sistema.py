from limite.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):

        self.__controlador_evento = None
        self.__controlador_organizador = None
        self.__controlador_participante = None
        self.__controlador_cartao_de_vacina = None
        self.__controlador_exame = None
        self.__controlador_registro_de_presenca = None
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

    @property
    def controlador_registro_de_presenca(self):
        return self.__controlador_registro_de_presenca


    def inicializar(self):
        self.abrir_menu_inicial()

    def abrir_menu_inicial(self):

        opcoes = {1: self.iniciar_modulo_eventos, 2: self.iniciar_modulo_organizadores,
                  3: self.iniciar_modulo_participantes, 4: self.iniciar_modulo_registro_de_presenca, 0: self.encerrar_sistema}

        while True:
            opcao_escolhida = self.tela.mostrar_menu_inicial()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()



    def iniciar_modulo_eventos(self):
        print("Modulo de eventos escolhido")
        

    def iniciar_modulo_organizadores(self):
        print("Modulo de organizadores escolhido")

    def iniciar_modulo_participantes(self):
        print("Modulo de participantes escolhido")

    def iniciar_modulo_registro_de_presenca(self):
        print("Módulo de registro de presenca escolhido")

    def encerrar_sistema(self):
        exit(0)