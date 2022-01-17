from entidade.evento import Evento
from entidade.endereco import Endereco
from controle.controlador import Controlador
from limite.tela_evento import TelaEvento


class ControladorEvento(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaEvento(self))

    def abrir_menu_inicial(self):

        opcoes = {1: self.cadastrar, 2: self.listar, 3: self.ver_detalhes}
        opcoes_validas = [0, 1, 2, 3]
        menu = self.tela.mostrar_menu_inicial

        self.listar()
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
            self.listar()

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