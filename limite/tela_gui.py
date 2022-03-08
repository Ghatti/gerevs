import PySimpleGUI as sg
from abc import ABC, abstractmethod


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

        if(button == sg.WIN_CLOSED):
            return (0, {})

        print(button)

        return button, values

    def close(self):
        self.window.Close()

    def mostrar_mensagem(self, mensagem: str, titulo="Mensagem"):
        sg.Popup(titulo, mensagem)
