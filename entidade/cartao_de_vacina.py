class Cartao_de_vacina:

    def __init__(self):
        self.__doses = []

    @property
    def doses(self):
        return self.__doses
    
    def registrar_dose(self, dose: int):
        pass