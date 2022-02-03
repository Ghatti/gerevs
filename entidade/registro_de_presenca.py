from entidade.pessoa import Pessoa


from entidade.linha_de_registro import LinhaDeRegistro


class RegistroDePresenca:

    def __init__(self, participante: Pessoa, entrada):
        self.__participante = participante
        self.__entrada = LinhaDeRegistro(entrada)
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

        registro_entrada = LinhaDeRegistro(entrada)

        if self.saida is not None:
            if(registro_entrada.data > self.saida.data):

                raise ValueError(
                    "A entrada não pode ser posterior à saída. Altere a saída primeiro ou informe outra entrada.")

        self.__entrada = registro_entrada

    @saida.setter
    def saida(self, saida: str):

        registro_saida = LinhaDeRegistro(saida)

        if(registro_saida.data < self.entrada.data):
            raise ValueError(
                "A saída não pode ser anterior à entrada. Altere a entrada primeiro ou informe outra saída")

        self.__saida = LinhaDeRegistro(saida)
