from limite.tela_sistema_gui import TelaSistemaGui


class TelaSistema:

    def __init__(self, controlador):
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador

    def mostrar_menu_inicial(self):
        tela = TelaSistemaGui()
        button, values = tela.open()
        tela.close()
        return button
