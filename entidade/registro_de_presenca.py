from entidade.evento import Evento
from entidade.participante import Participante

class RegistroDeṔresenca:

    def __init__(self, participante: Participante, evento: Evento):
        self.__participante = participante
        self.__evento = evento
        self.__entrada = None
        self.__saida = None
    
    @property
    def participante(self):
        return self.__participante
    
    @property
    def evento(self):
        return self.__evento
    
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
