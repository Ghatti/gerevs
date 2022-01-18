class CartaoDeVacina:

    def __init__(self, doses):
        self.__doses = doses

    @property
    def doses(self):
        return self.__doses

    def is_complete(self):

        return self.doses[0] and self.doses[1]

    def registrar_dose(self):

        if(self.doses[0]):
            self.__doses[1] = True
        else:
            self.__doses[0] == True
