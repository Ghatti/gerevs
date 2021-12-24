class Endereco:
    def __init__(self, cep: str, rua: str, numero: int, bairro: str, cidade: str, estado: str):
        self.__cep = cep
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cep(self):
        return self.__cep

    @property
    def rua(self):
        return self.__rua

    @property
    def numero(self):
        return self.__numero

    @property
    def bairro(self):
        return self.__bairro

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    @cep.setter
    def cep(self, cep: str):
        self.__cep = cep

    @rua.setter
    def rua(self, rua: str):
        self.__rua = rua

    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    @bairro.setter
    def bairro(self, bairro: str):
        self.__bairro = bairro

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @estado.setter
    def estado(self, estado: str):
        self.__estado = estado
