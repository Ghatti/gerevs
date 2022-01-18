from entidade.pessoa import Pessoa
from entidade.endereco import Endereco
from entidade.cartao_de_vacina import CartaoDeVacina
from entidade.exame import Exame


class Participante(Pessoa):

    def __init__(self, cpf: str, nome: str, nascimento: str, endereco, cartao_de_vacina=CartaoDeVacina):

        super().__init__(cpf, nome, nascimento, Endereco(endereco["cep"], endereco["rua"], endereco["numero"],
                                                         endereco["bairro"], endereco["cidade"], endereco["estado"]))
        self.__cartao_de_vacina = cartao_de_vacina
        self.__exames = []

    @property
    def cartao_de_vacina(self):
        return self.cartao_de_vacina

    @property
    def exames(self):
        return self.__exames

    def adicionar_exame(self, exame: Exame):
        pass
