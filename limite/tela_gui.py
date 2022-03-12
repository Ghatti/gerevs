import PySimpleGUI as sg
from abc import ABC, abstractmethod
from exceptions.cancelOperationException import CancelOperationException


class TelaGui(ABC):

    @abstractmethod
    def __init__(self):
        self.__window = None

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window

    def open(self):

        button, values = self.window.Read()

        if(button == sg.WIN_CLOSED or button == 0):
            self.window.close()
            raise CancelOperationException()
            # return (0, {})

        return button, values

    def close(self):
        self.window.Close()

    def mostrar_mensagem(self, mensagem: str, titulo="Mensagem"):
        sg.Popup(titulo, mensagem)
