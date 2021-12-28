class Controlador_sistema:

    def __init__(self):

        self.__controlador_evento = None
        self.__controlador_organizador = None
        self.__controlador_participante = None
        self.__controlador_cartao_de_vacina = None
        self.__controlador_exame = None
        self.__controlador_registro_de_presenca = None
        self.__tela = None

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
    def controlador_registro_de_presenca(self):
        return self.__controlador_registro_de_presenca

    def abrir_menu_inicial(self):
        pass

    def iniciar_modulo_eventos(self):
        pass

    def iniciar_modulo_organizadores(self):
        pass

    def iniciar_modulo_participantes(self):
        pass

    def iniciar_modulo_registro_de_presenca(self):
        pass