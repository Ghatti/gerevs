from dao.abstract_dao import AbstractDAO
from entidade.evento import Evento


class EventoDAO(AbstractDAO):

    def __init__(self):

        super().__init__("eventos.pkl")

    def add(self, evento: Evento):
        if(self.__evento_valido(evento)):
            super().add(evento.titulo, evento)

    def remove(self, evento: Evento())
    if(self.__evento_valido(evento)):
        super().remove(evento.titulo)

    def __evento_valido(self, evento):
        return (evento is not None) and (isinstance(evento, Evento) and isinstance(evento.titulo, str))
