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

    def abrir_menu_participantes(self):

        opcoes = {}
        opcoes_validas = [0]
        menu = self.tela.mostrar_menu_participantes

        self.abrir_menu(menu, opcoes, opcoes_validas)

    def abrir_menu_organizadores(self):

        opcoes = {}
        opcoes_validas = [0]
        menu = self.tela.mostrar_menu_participantes

        self.abrir_menu(menu, opcoes, opcoes_validas)

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

        self.abrir_menu_participantes()

    def listar_organizadores(self, evento):

        self.controlador_sistema.controlador_organizador.listar(
            evento.organizadores)

        self.abrir_menu_organizadores()
