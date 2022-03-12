from multiprocessing.sharedctypes import Value
import re
import PySimpleGUI as sg
from abc import ABC, abstractmethod
from datetime import datetime, time
from exceptions.validationException import ValidationException
from limite.tela_gui import TelaGui


class Tela(TelaGui, ABC):

    @abstractmethod
    def __init__(self, controlador):
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador

    # remove this method or turn abstract
    # by listing on the inicial menu, this method must go down on the hierarchy
    def mostrar_menu_inicial(self, entidades):

        pass

    # @abstractmethod

    def mostrar_tela_cadastro(self):
        pass

    # @abstractmethod
    def mostrar(self, entidade, i):
        pass

    # @abstractmethod
    def mostrar_detalhes(self, entidade):
        pass

    def confirmar(self, input_msg="Deseja confirmar a operação?"):
        confirmacao = sg.popup_yes_no(input_msg)

        return confirmacao == "Yes"

    def selecionar(self, opcoes):

        self.init_tela_selecao(opcoes)
        button, values = self.open()
        self.close()

        return values["row_index"][0]

    def validar_string(self, min=None, max=None, equal=None, formato=None, no_digit=None, opcoes=None):

        validators = []

        if(min is not None):
            def validar_minimo(valor):
                if not (len(valor) >= min):
                    raise ValidationException(
                        "O valor informado deve ter ao menos {} caracteres".format(min))
            validators.append(validar_minimo)

        if(max is not None):
            def validar_maximo(valor):
                if not (len(valor) <= max):
                    raise ValidationException(
                        "O valor informado deve ter no máximo {} caracteres".format(max))
            validators.append(validar_maximo)

        if(equal is not None):
            def validar_not_igual(valor):
                if (not len(valor) == equal):
                    raise ValidationException(
                        "O valor informado deve ter {} caracteres".format(equal))

            validators.append(validar_not_igual)

        if(formato is not None):
            def validar_formato(valor):
                if not re.match(formato, valor):
                    raise ValidationException(
                        "O valor informado não atende ao formato adequado")
            validators.append(validar_formato)

        if(opcoes is not None):
            def validar_opcoes(valor):
                if(valor.strip().lower() not in opcoes):
                    raise ValidationException(
                        "O valor informado não é uma opção válida."
                    )
            validators.append(validar_opcoes)

        if(no_digit is not None):
            def validar_no_digit(valor):
                if re.search('\d', valor):
                    raise ValidationException(
                        "O valor informado não deve conter números."
                    )
            validators.append(validar_no_digit)

        def run_validators(value):
            for validator in validators:
                validator(value)

        return run_validators

    def validar_inteiro(self, min=None, max=None, opcoes=None):

        validators = []

        if(min is not None):

            def validar_minimo(valor):
                if valor < min:
                    raise ValidationException(
                        "O valor informado não pode ser menor que {}".format(min))
            validators.append(validar_minimo)

        if(max is not None):
            def validar_maximo(valor):
                if valor > max:
                    raise ValidationException(
                        "O valor informado não pode ser maior que {}".format(max))
            validators.append(validar_maximo)

        if(opcoes is not None):
            def validar_opcao(valor):
                if valor not in opcoes:
                    raise ValidationException(
                        "A opção informada não é válida."
                    )
            validators.append(validar_opcao)

        def run_validators(value):

            try:
                value = int(value)
            except ValueError as err:
                raise ValidationException("O valor informado não é um inteiro")
            for validator in validators:
                validator(value)

        return run_validators

    def validar_data(self, min=None, max=None, delta=None):
        # Error messages need improvement
        validators = []
        if(min is not None):
            def validar_minimo(valor):
                if(valor < min):
                    raise ValidationException(
                        "A data informada é anterior à data mínima: {}".format(
                            min.date().strftime("%d/%m/%Y")))
            validators.append(validar_minimo)

        if(max is not None):
            def validar_maximo(valor):
                if(valor > max):
                    raise ValidationException(
                        "A data informada é posterior à data máxima: {}".format(max.date().strftime("%d/%m/%Y")))
            validators.append(validar_maximo)

        if(delta is not None):
            def validar_delta(valor):
                if(datetime.today() - valor > delta):
                    raise ValidationException(
                        "A data informada é muito antiga. Informe uma data mais recente.")

            validators.append(validar_delta)

        def run_validators(value):

            try:
                value = datetime.strptime(
                    value, "%d/%m/%Y")
            except ValueError:
                raise ValidationException(
                    "A data informada não é válida, utilize o formado dd/m/aaaa.")

            for validator in validators:
                validator(value)

        return run_validators
