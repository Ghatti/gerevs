from datetime import datetime, timedelta

from entidade.evento import Evento
from entidade.endereco import Endereco
from controle.controlador import Controlador
from entidade.registro_de_presenca import RegistroDeṔresenca
from limite.tela_evento import TelaEvento


class ControladorEvento(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaEvento(self))

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar, 2: self.ver_todos,
                  3: self.ver_detalhes, 4: self.ver_futuros, 5: self.ver_realizados}
        opcoes_validas = [0, 1, 2, 3, 4, 5]
        menu = self.tela.mostrar_menu_inicial

        self.ver_todos()
        self.abrir_menu(menu, opcoes, opcoes_validas)

    def abrir_menu_visualizacao(self, entidade):

        opcoes = {1: self.alterar, 2: self.remover,
                  3: self.abrir_menu_listar_participantes, 4: self.listar_organizadores}
        opcoes_validas = [0, 1, 2, 3, 4]
        menu = self.tela.mostrar_menu_visualizacao

        self.abrir_menu(menu, opcoes, opcoes_validas, entidade)

    def abrir_menu_listar_participantes(self, evento):

        opcoes = {1: lambda: self.listar_participantes(evento), 2: lambda: self.listar_participantes(
            evento, False), 3: lambda: self.listar_participantes(evento, True)}
        opcoes_validas = [0, 1, 2, 3]

        menu = self.tela.mostrar_menu_listar_participantes

        self.abrir_menu(menu, opcoes, opcoes_validas)

    def abrir_menu_participantes(self, evento):

        opcoes = {1: self.adicionar_participante,
                  2: self.remover_participante, 3: self.abrir_menu_confirmar_participante, 4: self.abrir_menu_registros}
        opcoes_validas = [0, 1, 2, 3, 4]
        menu = self.tela.mostrar_menu_participantes

        self.abrir_menu(menu, opcoes, opcoes_validas, evento)

    def abrir_menu_registros(self, evento):

        opcoes = {1: self.listar_registros_de_presenca, 2: self.ver_registro_de_presenca,
                  3: self.registrar_entrada, 4: self.registrar_saida}
        opcoes_validas = [0, 1, 2, 3, 4]
        menu = self.tela.mostrar_menu_registros

        self.abrir_menu(menu, opcoes, opcoes_validas, evento)

    def abrir_menu_organizadores(self, evento):

        opcoes = {1: self.adicionar_organizador, 2: self.remover_organizador}
        opcoes_validas = [0, 1, 2]
        menu = self.tela.mostrar_menu_organizadores

        self.abrir_menu(menu, opcoes, opcoes_validas, evento)

    def abrir_menu_confirmar_participante(self, evento):
        opcoes = {1: lambda evento: self.confirmar_participante(
            evento, True), 2: lambda evento: self.confirmar_participante(evento, False)}
        opcoes_validas = [0, 1, 2]
        menu = self.tela.mostrar_menu_confirmar_participantes

        self.abrir_menu(menu, opcoes, opcoes_validas, evento)

    def cadastrar(self):

        try:

            if(not self.controlador_sistema.controlador_organizador.tem_entidades()):
                raise ValueError(
                    "Não é possível cadastrar um evento porque ainda não há organizadores cadastrados")

            dados = self.tela.mostrar_tela_cadastro()
            dados["organizador"] = self.controlador_sistema.controlador_organizador.selecionar(
                listar=True)

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

    def remover(self, evento):

        confirmacao = self.tela.confirmar()
        if(confirmacao):
            self.entidades.remove(evento)

    def ver_futuros(self):

        hoje = datetime.today()

        eventos_futuros = []

        for evento in self.entidades:
            if evento.data > hoje:
                eventos_futuros.append(evento)

        self.listar(eventos_futuros)

    def ver_realizados(self):

        hoje = datetime.today()

        eventos_realizados = []

        for evento in self.entidades:
            if evento.data < hoje:
                eventos_realizados.append(evento)

        self.listar(eventos_realizados)

    def listar_participantes(self, evento, filtro=None):

        if (filtro is None):
            participantes = evento.get_all_participantes()
        elif (filtro == False):
            participantes = evento.participantes_a_confirmar
        else:
            participantes = evento.participantes_confirmados

        self.controlador_sistema.controlador_participante.listar(
            participantes)

        self.abrir_menu_participantes(evento)

    def adicionar_participante(self, evento):

        participantes_registrados = evento.get_all_participantes()

        if(len(participantes_registrados) == evento.capacidade):
            self.tela.mostrar_mensagem("Evento lotado!")
        else:

            participante = self.controlador_sistema.controlador_participante.selecionar(
                listar=True)

            if(participante not in participantes_registrados):
                evento.participantes_a_confirmar.append(participante)
                self.tela.mostrar_mensagem("Participante incluído!")
            else:
                # mudar para erro?
                self.tela.mostrar_mensagem(
                    "Participante já registrado no evento.")

    def remover_participante(self, evento):

        participantes_registrados = evento.get_all_participantes()

        self.controlador_sistema.controlador_participante.listar(
            participantes_registrados)

        opcao = self.abrir_tela_selecionar()
        participante = participantes_registrados[opcao-1]

        if(participante in evento.participantes_a_confirmar):
            evento.participantes_a_confirmar.remove(participante)
        else:
            evento.participantes_confirmados.remove(participante)

        self.tela.mostrar_mensagem("Participante removido!")

    def confirmar_participante(self, evento, modo=True):

        # exibe participantes não confirmados

        self.controlador_sistema.controlador_participante.listar(
            evento.participantes_a_confirmar)

        # pede seleção de um participante

        opcao = self.abrir_tela_selecionar()
        participante = evento.participantes_a_confirmar[opcao-1]

        # verifica vacinação

        if(modo):
            confirmacao = participante.cartao_de_vacina.is_complete()
        else:
            confirmacao = self.confirmar_com_exame(
                evento.data, participante.exame)

        if(confirmacao):
            # remove participante da lista de a confirmar
            evento.participantes_a_confirmar.remove(participante)
        # inclui na lista de participantes confirmados
            evento.participantes_confirmados.append(participante)
            self.tela.mostrar_mensagem("Participante confirmado!")
        else:
            self.tela.mostrar_mensagem(
                "Participante não completou os requisitos para confirmação")

    def confirmar_com_exame(self, data_evento, exame):

        prazo = data_evento - exame.data
        if(not exame.resultado and prazo <= timedelta(days=3)):
            return True

        return False

    def listar_registros_de_presenca(self, evento):

        if(len(evento.registros_de_presenca) == 0):
            self.tela.mostrar_mensagem(
                "Não há registros de presença cadastrados.")
        else:
            for i, registro in enumerate(evento.registros_de_presenca):
                self.tela.mostrar_registro(registro, i)

    def ver_registro_de_presenca(self, evento):

        registro = self.selecionar(lista=evento.registros_de_presenca)
        self.tela.mostrar_detalhes_registro(registro)

    def registrar_entrada(self, evento):

        # na lista de participantes, o usuário seleciona a opção registrar entrada
        #   Não havendo, exibe mensagem de que não há participantes confirmados.

        if(len(evento.participantes_confirmados) == 0):
            self.tela.mostrar_mensagem(
                "Não há participantes confirmados para o evento.")
        else:

            # Sistema solicita a seleção de um participante para registrar a entrada
            participante = self.selecionar(
                listar=True, lista=evento.participantes_confirmados)

        # Sistema verifica se participante já tem registro de entrada.
        # Positivo, informa o usuário de que a entrada já foi registrada e retorna
            for registro in evento.registros_de_presenca:
                if registro.participante == participante:
                    self.tela.mostrar_mensagem(
                        "Participante já possui registro de entrada.")
                    return

        # Sistema solicita o horário da entrada.

            entrada = self.tela.mostrar_tela_registrar_entrada(
                evento.data, evento.horario)

        # Sistema cria o registro de presença e insere no evento
            registro = RegistroDeṔresenca(participante, entrada)
            evento.adicionar_registro_de_presenca(registro)

    def registrar_saida(self, evento):

        # na lista de participantes, o usuário seleciona a opção registrar saída
        # Não havendo registros de presença, exibe mensagem de que ainda não foram registradas entrada
        # Sistema lista os registros de entrada já cadastrados
        # Sistema solicita a seleção de um paritipante para registrar a saída
        # Sistema solicita o horário da saída
        # SIstema insere a saída no registro

        if(len(evento.registros_de_presenca) == 0):
            self.tela.mostrar_mensagem(
                "Ainda não foi registrada a entrada de nenhum participante")

        else:

            self.listar_registros_de_presenca(evento)
            registro = self.selecionar(lista=evento.registros_de_presenca)

            if(registro.saida is not None):
                self.tela.mostrar_mensagem(
                    "A saída deste participante já foi registrada")
                return

            saida = self.tela.mostrar_tela_registrar_entrada(
                evento.data, evento.horario)

            registro.saida = saida

    def listar_organizadores(self, evento):

        self.controlador_sistema.controlador_organizador.listar(
            evento.organizadores)

        self.abrir_menu_organizadores(evento)

    def adicionar_organizador(self, evento):

        organizador = self.controlador_sistema.controlador_organizador.selecionar(
            listar=True)

        if(organizador not in evento.organizadores):
            evento.organizadores.append(organizador)
            self.tela.mostrar_mensagem("Organizador incluído!")
        else:
            # mudar para erro?
            self.tela.mostrar_mensagem("Organizador já registrado no evento.")

    def remover_organizador(self, evento):

        if(len(evento.organizadores) == 1):
            self.tela.mostrar_mensagem(
                "Evento possui apenas um organizador. É necessário adicionar outro organizador antes de removê-lo.")
        else:
            self.controlador_sistema.controlador_organizador.listar(
                evento.organizadores)

            opcao = self.abrir_tela_selecionar()
            evento.organizadores.pop(opcao-1)

            self.tela.mostrar_mensagem("Organizador removido!")
