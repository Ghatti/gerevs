from dao.abstract_dao import AbstractDAO
from entidade.evento import Evento
# from dao.organizador_dao import OrganizadorDAO
# from dao.participante_dao import ParticipanteDAO


class EventoDAO(AbstractDAO):

    def __init__(self):

        super().__init__("eventos.pkl")

    def persist(self, evento: Evento):
        if(self.__evento_valido(evento)):
            super().persist(evento.titulo, evento)

    def remove(self, evento: Evento):
        if(self.__evento_valido(evento)):
            super().remove(evento.titulo)

    def __evento_valido(self, evento):
        return (evento is not None) and (isinstance(evento, Evento) and isinstance(evento.titulo, str))

    def update_pessoa(self, pessoa):

        print(pessoa.nome)

        for evento in self.get_all():

            for i, participante in enumerate(evento.participantes_a_confirmar):
                if(participante.cpf == pessoa.cpf):
                    evento.participantes_a_confirmar[i] = pessoa

            for i, participante in enumerate(evento.participantes_confirmados):
                if(participante.cpf == pessoa.cpf):
                    evento.participantes_confirmados[i] = pessoa

            for i, organizador in enumerate(evento.organizadores):
                if(organizador.cpf == pessoa.cpf):
                    evento.organizadores[i] = pessoa

            self.persist(evento)
