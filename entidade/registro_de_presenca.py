from entidade.evento import Evento
from entidade.participante import Participante

class RegistroDeṔresenca:

    def __init__(self, participante: Participante, entrada):
        self.__participante = participante
        self.__entrada = entrada
        self.__saida = None
    
    @property
    def participante(self):
        return self.__participante
    
    @property
    def entrada(self):
        return self.__entrada
    
    @property
    def saida(self):
        return self.__saida
    
    @entrada.setter
    def entrada(self, entrada: str):
        self.__entrada = entrada
    
    @saida.setter
    def saida(self, saida: str):
        self.__saida = saida
