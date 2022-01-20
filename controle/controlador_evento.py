from datetime import timedelta

from entidade.evento import Evento
from entidade.endereco import Endereco
from controle.controlador import Controlador
from limite.tela_evento import TelaEvento


class ControladorEvento(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaEvento(self))

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar, 2: self.ver_todos,
                  3: self.ver_detalhes}
        opcoes_validas = [0, 1, 2, 3]
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

    def abrir_menu_participantes(self, evento, filtro):

        opcoes = {1: self.adicionar_participante,
                  2: self.remover_participante, 3: self.abrir_menu_confirmar_participante}
        opcoes_validas = [0, 1, 2, 3]
        menu = self.tela.mostrar_menu_participantes

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
                raise ValueError

            dados = self.tela.mostrar_tela_cadastro()
            dados["organizador"] = self.controlador_sistema.controlador_organizador.selecionar(
                listar=True)
            print(dados)

            # Cadastrar evento
            novo_evento = Evento(dados["titulo"], dados["data"], dados["horario"],
                                 dados["endereco"], dados["capacidade"], dados["organizador"])

            self.entidades.append(novo_evento)
            self.tela.mostrar_mensagem("Evento cadastrado!")
            self.ver_todos()

        except ValueError:

            self.tela.mostrar_mensagem(
                "Não é possível cadastrar um evento porque ainda não há organizadores cadastrados")

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

    def listar_participantes(self, evento, filtro=None):

        if (filtro is None):
            participantes = evento.get_all_participantes()
        elif (filtro == False):
            participantes = evento.participantes_a_confirmar
        else:
            participantes = evento.participantes_confirmados

        self.controlador_sistema.controlador_participante.listar(
            participantes)

        self.abrir_menu_participantes(evento, filtro)

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
                self.tela.mostrar_mensage(
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
        if(not exame.resultado and prazo <= timedelta(days=2)):
            return True

        return False

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
            self.tela.mostrar_mensage("Organizador já registrado no evento.")

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
