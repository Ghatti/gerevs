from pessoa import Pessoa
from endereco import Endereco

class Participante(Pessoa):

    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: Endereco, cartao_de_vacina):

        super().__init__(cpf, nome, nascimento, endereco)
        self.__cartao_de_vacina = cartao_de_vacina
        self.__exames = []

    @property
    def cartao_de_vacina(self):
        return self.cartao_de_vacina 
    
    @property
    def exames(self):
        return self.__exames

    def adicionar_exame(self, exame):
        pass