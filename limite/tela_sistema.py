class TelaSistema:

    def __init__(self, controlador):
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador
    
    def mostrar_menu_inicial(self):
        print("------ Sistema de Gerenciamento de Eventos ------")
        print("Escolha sua opção:")
        print("1 - Iniciar módulo de Eventos")
        print("2 - Iniciar módulo de Organizadores")
        print("3 - Iniciar módulo de Participantes")
        print("4 - Iniciar módulo de Registro de Presença")
        print("0 - Encerrar Sistema")

        opcoes = range(5)

        while True:
            opcao = input("Escolha a opcao:")

            try:
                opcao = int(opcao)
                if(opcao not in opcoes):
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor incorreto. Digite um valor numérico válido.")