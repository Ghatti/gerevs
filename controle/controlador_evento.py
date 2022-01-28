from datetime import datetime, timedelta
from multiprocessing.sharedctypes import Value
from controle import controlador_sistema
from entidade.evento import Evento
from controle.controlador import Controlador
from entidade.registro_de_presenca import RegistroDeṔresenca
from limite.tela_evento import TelaEvento


class ControladorEvento(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaEvento(self))

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar, 2: self.abrir_menu_listar,
                  3: self.ver_detalhes}
        menu = self.tela.mostrar_menu_inicial

        self.ver_todos()
        self.abrir_menu(menu, opcoes)

    def abrir_menu_visualizacao(self, entidade):

        opcoes = {1: self.alterar, 2: self.remover,
                  3: self.gerenciar_participantes, 4: self.gerenciar_organizadores, 5: self.gerenciar_registros_de_presenca}

        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes,  entidade)

    def abrir_menu_visualizacao_registro(self, registro):

        opcoes = {1: self.alterar_registro_de_presenca,
                  2: self.remover_registro_de_presenca}

        menu = self.tela.mostrar_menu_visualizacao_registro

        self.abrir_menu(menu, opcoes, registro)

    def abrir_menu_listar(self):
        opcoes = {1: self.ver_todos, 2: self.ver_futuros,
                  3: self.ver_realizados, 4: self.ver_ranking}

        menu = self.tela.mostrar_menu_listar

        self.abrir_menu(menu, opcoes)

    def abrir_menu_listar_participantes(self, evento):

        opcoes = {1: lambda: self.listar_participantes(evento), 2: lambda: self.listar_participantes(
            evento, False), 3: lambda: self.listar_participantes(evento, True)}

        menu = self.tela.mostrar_menu_listar_participantes

        self.abrir_menu(menu, opcoes)

    def abrir_menu_participantes(self, evento):

        opcoes = {1: self.adicionar_participante,
                  2: self.remover_participante, 3: self.abrir_menu_listar_participantes, 4: self.confirmar_participante}

        menu = self.tela.mostrar_menu_participantes

        self.abrir_menu(menu, opcoes, evento)

    def abrir_menu_registros(self, evento):

        opcoes = {1: self.listar_registros_de_presenca, 2: self.ver_registro_de_presenca,
                  3: self.registrar_entrada, 4: self.registrar_saida}

        menu = self.tela.mostrar_menu_registros

        self.abrir_menu(menu, opcoes, evento)

    def abrir_menu_organizadores(self, evento):

        opcoes = {1: self.adicionar_organizador,
                  2: self.remover_organizador, 3: self.listar_organizadores}

        menu = self.tela.mostrar_menu_organizadores

        self.abrir_menu(menu, opcoes, evento)

        self.abrir_menu(menu, opcoes, evento)

    def gerenciar_organizadores(self, evento):

        self.listar_organizadores(evento)
        self.abrir_menu_organizadores(evento)

    def gerenciar_participantes(self, evento):
        self.listar_participantes(evento)
        self.abrir_menu_participantes(evento)

    def gerenciar_registros_de_presenca(self, evento):
        self.listar_registros_de_presenca(evento)
        self.abrir_menu_registros(evento)

    def cadastrar(self):

        try:

            if(not self.controlador_sistema.controlador_organizador.tem_entidades()):

                cadastrar_org = self.tela.ler_string(
                    "Não é possível cadastrar um evento porque ainda não há organizadores cadastrados. Deseja cadastrar um organizador primeiro? (s/n)", self.tela.validar_string(opcoes=["s", "n"]))

                if(cadastrar_org == "s"):
                    self.controlador_sistema.controlador_organizador.cadastrar()
                    self.tela.mostrar_mensagem(
                        "Agora, vamos continuar o cadastro do evento.")
                else:
                    raise ValueError(
                        "Como não há organizadores registrados, não será possível cadastrar um evento.")

            dados = self.tela.mostrar_tela_cadastro()
            dados["organizador"] = self.controlador_sistema.controlador_organizador.selecionar()

            # Cadastrar evento
            novo_evento = Evento(dados["titulo"], dados["data"], dados["horario"],
                                 dados["endereco"], dados["capacidade"], dados["organizador"])

            self.entidades.append(novo_evento)
            self.tela.mostrar_mensagem("Evento cadastrado!")
            self.ver_todos()

        except ValueError as err:

            self.tela.mostrar_mensagem(err)

    def alterar(self, evento):

        dados = self.tela.mostrar_tela_cadastro(alterar=True)

        evento.titulo = dados["titulo"]
        evento.data = dados["data"]
        evento.horario = dados["horario"]
        evento.endereco = dados["endereco"]
        evento.capacidade = dados["capacidade"]

        self.tela.mostrar_detalhes(evento)

    def ver_ranking(self):

        try:

            sorted_eventos = sorted(self.entidades, key=lambda evento: len(
                evento.get_all_participantes()), reverse=True)
            self.listar(sorted_eventos)

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def ver_futuros(self):

        try:
            hoje = datetime.today()

            eventos_futuros = []

            for evento in self.entidades:
                if evento.data > hoje:
                    eventos_futuros.append(evento)

                self.listar(eventos_futuros)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def ver_realizados(self):
        try:
            hoje = datetime.today()

            eventos_realizados = []

            for evento in self.entidades:
                if evento.data < hoje:
                    eventos_realizados.append(evento)

            self.listar(eventos_realizados)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def listar_participantes(self, evento, filtro=None):
        try:
            if (filtro is None):
                participantes = evento.get_all_participantes()
            elif (filtro == False):
                participantes = evento.participantes_a_confirmar
            else:
                participantes = evento.participantes_confirmados

            self.controlador_sistema.controlador_participante.listar(
                participantes)

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def adicionar_participante(self, evento):
        try:
            participantes_registrados = evento.get_all_participantes()

            if(len(participantes_registrados) == evento.capacidade):
                raise ValueError("O evento já está lotado.")

            participante = self.controlador_sistema.controlador_participante.selecionar()

            if(participante not in participantes_registrados):
                evento.adicionar_participante(participante)
                self.tela.mostrar_mensagem("Participante incluído!")
            else:
                raise ValueError("Participante já registrado no evento.")
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def remover_participante(self, evento):
        try:
            participantes_registrados = evento.get_all_participantes()

            participante = self.controlador_sistema.controlador_participante.selecionar(
                participantes_registrados)

            evento.remover_participante(participante)

            self.tela.mostrar_mensagem("Participante removido!")

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def confirmar_participante(self, evento):
        try:
            # exibe participantes não confirmados
            # pede seleção de um participante

            participante = self.controlador_sistema.controlador_participante.selecionar(
                evento.participantes_a_confirmar)

            self.tela.mostrar_menu_confirmar_participantes()
            modo = self.tela.ler_inteiro(
                validators=self.tela.validar_inteiro(opcoes=[1, 2])) == 1
            # verifica vacinação

            if(modo):
                confirmacao = participante.cartao_de_vacina.is_complete()
            else:
                confirmacao = self.confirmar_com_exame(
                    evento.data, participante.exame)

            if(confirmacao):
                # remove participante da lista de a confirmar
                # inclui na lista de participantes confirmados
                evento.confirmar_participante(participante)
                self.tela.mostrar_mensagem("Participante confirmado!")
            else:
                raise ValueError(
                    "Participante não completou os requisitos para confirmação")

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def confirmar_com_exame(self, data_evento, exame):

        prazo = data_evento - exame.data
        if(not exame.resultado and prazo <= timedelta(days=3)):
            return True

        return False

    def listar_organizadores(self, evento):

        try:
            self.controlador_sistema.controlador_organizador.listar(
                evento.organizadores)

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def adicionar_organizador(self, evento):
        try:
            organizador = self.controlador_sistema.controlador_organizador.selecionar()

            if(organizador in evento.organizadores):
                raise ValueError("Organizador já registrado no evento.")

            evento.adicionar_organizador(organizador)
            self.tela.mostrar_mensagem("Organizador incluído!")
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def remover_organizador(self, evento):
        try:

            if(len(evento.organizadores) == 1):
                raise ValueError(
                    "Evento possui apenas um organizador. É necessário adicionar outro organizador antes de removê-lo.")

            organizador = self.controlador_sistema.controlador_organizador.selecionar(
                evento.organizadores)

            evento.remover_organizador(organizador)

            self.tela.mostrar_mensagem("Organizador removido!")
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def listar_registros_de_presenca(self, evento):
        try:
            if(len(evento.registros_de_presenca) == 0):
                raise ValueError(
                    "Não há registros de presença cadastrados.")

            for i, registro in enumerate(evento.registros_de_presenca):
                self.tela.mostrar_registro(registro, i+1)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def ver_registro_de_presenca(self, evento):
        try:
            registro = self.selecionar(
                evento.registros_de_presenca, listar=False)
            self.tela.mostrar_detalhes_registro(registro)
            self.abrir_menu_visualizacao_registro(registro)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def registrar_entrada(self, evento):

        delta_limit = timedelta(days=1)
        # na lista de participantes, o usuário seleciona a opção registrar entrada
        #   Não havendo, exibe mensagem de que não há participantes confirmados.
        try:

            if(len(evento.participantes_confirmados) == 0):
                raise ValueError(
                    "Não há participantes confirmados para o evento.")

            # Sistema solicita a seleção de um participante para registrar a entrada
            participante = self.controlador_sistema.controlador_participante.selecionar(
                evento.participantes_confirmados)

            # Sistema verifica se participante já tem registro de entrada.
            # Positivo, informa o usuário de que a entrada já foi registrada e retorna
            for registro in evento.registros_de_presenca:
                if registro.participante == participante:
                    raise ValueError(
                        "Participante já possui registro de entrada.")

            # Sistema solicita o horário da entrada.

            entrada = self.tela.mostrar_tela_registrar_presenca(
                evento.data, evento.horario, delta_limit)

            # Sistema cria o registro de presença e insere no evento
            registro = RegistroDeṔresenca(participante, entrada)
            evento.adicionar_registro_de_presenca(registro)

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def registrar_saida(self, evento):

        # na lista de participantes, o usuário seleciona a opção registrar saída
        # Não havendo registros de presença, exibe mensagem de que ainda não foram registradas entrada
        # Sistema lista os registros de entrada já cadastrados
        # Sistema solicita a seleção de um paritipante para registrar a saída
        # Sistema solicita o horário da saída
        # SIstema insere a saída no registro

        delta_limit = timedelta(days=1)

        try:

            if(len(evento.registros_de_presenca) == 0):
                raise ValueError(
                    "Ainda não foi registrada a entrada de nenhum participante")

            self.listar_registros_de_presenca(evento)
            registro = self.selecionar(
                evento.registros_de_presenca, listar=False)

            if(registro.saida is not None):
                raise ValueError(
                    "A saída deste participante já foi registrada")

            saida = self.tela.mostrar_tela_registrar_presenca(
                evento.data, evento.horario, delta_limit, entrada=False)

            if(saida["data"] < registro.entrada["data"] or (saida["data"] == registro.entrada["data"] and saida["horario"] < registro.entrada["horario"])):
                raise ValueError("A saída informada é anterior à entrada.")

            registro.saida = saida

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def alterar_registro_de_presenca(self, registro):
        print("Alterar registro")

# do not work
    def remover_registro_de_presenca(self, registro):
        confirmacao = self.tela.confirmar()
        if(confirmacao):
            self.entidades.registros_de_presenca.remove(registro)
