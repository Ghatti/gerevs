from entidade.pessoa import Pessoa


from entidade.linha_de_registro import LinhaDeRegistro


class RegistroDeṔresenca:

    def __init__(self, participante: Pessoa, entrada):
        self.__participante = participante
        self.__entrada = LinhaDeRegistro(entrada["data"], entrada["horario"])
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

        registro_entrada = LinhaDeRegistro(entrada["data"], entrada["horario"])

        if self.saida is not None:
            if(registro_entrada.data > self.saida.data or (registro_entrada.data == self.saida.data and registro_entrada.horario > self.saida.horario)):

                raise ValueError(
                    "A entrada não pode ser posterior à saída. Altere a saída primeiro ou informe outra entrada.")

        self.__entrada = registro_entrada

    @saida.setter
    def saida(self, saida: str):

        registro_saida = LinhaDeRegistro(saida["data"], saida["horario"])

        if(registro_saida.data < self.entrada.data or (registro_saida.data == self.entrada.data and registro_saida.horario < self.entrada.horario)):
            raise ValueError(
                "A saída não pode ser anterior à entrada. Altere a entrada primeiro ou informe outra saída")

        self.__saida = LinhaDeRegistro(saida["data"], saida["horario"])
