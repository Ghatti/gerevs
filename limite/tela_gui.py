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

    @abstractmethod
    def init_components(self):
        pass

    def open(self):

        button, values = (None, None)

        button, value = self.window.Read()

        if(button == sg.WIN_CLOSED):
            return (0, {})

        return button, values

    def close(self):
        self.window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
