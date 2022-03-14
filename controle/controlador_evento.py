from datetime import datetime, timedelta

from entidade.evento import Evento
from controle.controlador import Controlador
from exceptions.validationException import ValidationException
from limite.tela_evento import TelaEvento
from entidade.registro_de_presenca import RegistroDePresenca
from dao.evento_dao import EventoDAO
from exceptions.cancelOperationException import CancelOperationException


class ControladorEvento(Controlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaEvento(self), EventoDAO())

    def abrir_menu_inicial(self):

        opcoes = {1: lambda input: self.cadastrar(),
                  2: lambda input: self.alterar(input), 3: lambda input: self.ver_detalhes(input), 4: lambda input: self.remover(input),
                  5: lambda input: self.ver_futuros(), 6: lambda input: self.ver_realizados(), 7: lambda input: self.ver_ranking()}

        def menu():
            entidades = [self.unpack(entidade) for entidade in self.entidades]
            return self.tela.mostrar_menu_inicial(entidades)

        self.abrir_menu(menu, opcoes)

    def abrir_menu_visualizacao(self, entidade):

        opcoes = {1: self.abrir_menu_participantes,
                  2: self.abrir_menu_organizadores, 3: self.abrir_menu_registros}

        def menu():
            return self.tela.mostrar_detalhes(self.unpack(entidade))

        self.abrir_menu(menu, opcoes,  entidade)

    def abrir_menu_visualizacao_registro(self, evento, registro):

        opcoes = {1: lambda: self.alterar_registro_de_presenca(evento, registro),
                  2: lambda: self.remover_registro_de_presenca(evento, registro)}

        menu = self.tela.mostrar_menu_visualizacao_registro

        self.abrir_menu(menu, opcoes)

    def abrir_menu_listar_participantes(self, evento):
        try:
            if(len(evento.get_all_participantes()) == 0):
                raise ValueError("O evento não possui participantes")

            opcoes = {1: lambda: self.listar_participantes(evento), 2: lambda: self.listar_participantes(
                evento, False), 3: lambda: self.listar_participantes(evento, True)}

            menu = self.tela.mostrar_menu_listar_participantes

            self.abrir_menu(menu, opcoes)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def abrir_menu_participantes(self, evento):

        opcoes = {1: lambda entidade, input: self.adicionar_participante(entidade),
                  2: self.remover_participante, 3: lambda entidade, input: self.abrir_menu_confirmar_participantes(entidade, False),
                  4: lambda entidade, input: self.abrir_menu_confirmar_participantes(entidade, True)}

        def menu():
            part_list = self.listar_participantes(evento)
            return self.tela.mostrar_menu_participantes(part_list)

        self.abrir_menu(menu, opcoes, evento, True)

    def abrir_menu_confirmar_participantes(self, evento, filtro):

        opcoes = {1: lambda entidade, input: self.confirmar_participante(
            entidade, input, True), 2: lambda entidade, input: self.confirmar_participante(entidade, input, False)}

        def menu():
            part_list = self.listar_participantes(evento, filtro)
            return self.tela.mostrar_tela_listar_participantes(part_list, confirmar=filtro)

        self.abrir_menu(menu, opcoes, evento, True)

    def abrir_menu_registros(self, evento):

        opcoes = {
            1: lambda entidade, input: self.registrar_entrada(entidade), 2: self.registrar_saida, 3: self.alterar_registro_de_presenca, 4: self.remover_registro_de_presenca}

        def menu():
            return self.tela.mostrar_menu_registros([self.unpack_registro(registro) for registro in evento.registros_de_presenca])

        self.abrir_menu(menu, opcoes, evento, True)

    def abrir_menu_organizadores(self, evento):

        opcoes = {1: lambda entidade, input: self.adicionar_organizador(entidade),
                  2: self.remover_organizador}

        def menu():
            org_list = self.listar_organizadores(evento)
            return self.tela.mostrar_menu_organizadores(org_list)

        self.abrir_menu(menu, opcoes, evento, True)

    def cadastrar(self):

        try:

            if(not self.controlador_sistema.controlador_organizador.tem_entidades()):

                self.tela.mostrar_mensagem(
                    "Não há organizadores registrados, você será redirecionado para o registro de organizadores.", "Alerta")
                self.controlador_sistema.controlador_organizador.cadastrar()

                if(self.controlador_sistema.controlador_organizador.tem_entidades()):
                    self.tela.mostrar_mensagem(
                        "Agora, vamos continuar o cadastro do evento.", "Alerta")
                else:
                    raise ValueError(
                        "Como não há organizadores registrados, não será possível cadastrar um evento.")

            dados = self.tela.mostrar_tela_cadastro()

            organizador = self.controlador_sistema.controlador_organizador.selecionar()

            dados["organizador"] = organizador

            if(dados["organizador"].nascimento > dados["data"]):
                raise ValidationException(
                    "O organizador escolhido nasceu após o evento ser realizado. Tente novamente")

            dados["endereco"] = {
                "cep": dados["cep"],
                "rua": dados["rua"],
                "numero": dados["numero"],
                "bairro": dados["bairro"],
                "cidade": dados["cidade"],
                "estado": dados["estado"],
            }

            # Cadastrar evento
            novo_evento = Evento(dados["titulo"], dados["data"],
                                 dados["endereco"], dados["capacidade"], dados["organizador"])

            self.dao.persist(novo_evento)
            self.tela.mostrar_mensagem("Evento cadastrado!")

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

        except CancelOperationException as err:
            self.tela.mostrar_mensagem(err)

    def alterar(self, dados):
        try:
            evento = self.get_entidade(dados["row_index"])

            dados = self.tela.mostrar_tela_cadastro(
                self.unpack(evento), alterar=True)

            dados["endereco"] = {
                "cep": dados["cep"],
                "rua": dados["rua"],
                "numero": dados["numero"],
                "bairro": dados["bairro"],
                "cidade": dados["cidade"],
                "estado": dados["estado"]
            }

            evento.data = dados["data"]
            evento.endereco = dados["endereco"]

            self.dao.persist(evento)
        except CancelOperationException as err:
            self.tela.mostrar_mensagem(err)
        except ValidationException as err:
            self.tela.mostrar_mensagem(err)

    def ver_ranking(self):

        try:

            sorted_eventos = sorted(self.entidades, key=lambda evento: len(
                evento.get_all_participantes()), reverse=True)
            event_list = self.listar(sorted_eventos)
            self.tela.mostrar_tela_listar(
                event_list, "Ranking por Participantes")

        except CancelOperationException as err:
            pass
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def ver_futuros(self):

        try:
            hoje = datetime.today()

            eventos_futuros = []

            for evento in self.entidades:

                if evento.data > hoje:
                    eventos_futuros.append(evento)

            event_list = self.listar(eventos_futuros)
            self.tela.mostrar_tela_listar(event_list, "Eventos Futuros")
        except CancelOperationException as err:
            pass
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def ver_realizados(self):
        try:
            hoje = datetime.today()

            eventos_realizados = []

            for evento in self.entidades:
                if evento.data < hoje:
                    eventos_realizados.append(evento)

            event_list = self.listar(eventos_realizados)
            self.tela.mostrar_tela_listar(event_list, "Eventos Realizados")
        except CancelOperationException as err:
            pass
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def listar_participantes(self, evento, filtro=None):
        try:
            if (filtro is None):
                participantes = evento.get_all_participantes()
            elif (filtro == True):
                participantes = evento.participantes_a_confirmar
            else:
                participantes = evento.participantes_confirmados

            return self.controlador_sistema.controlador_participante.listar(
                participantes)

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def adicionar_participante(self, evento):
        try:
            participantes_registrados = evento.get_all_participantes()
            cpfs = [participante.cpf for participante in participantes_registrados]

            if(len(participantes_registrados) == evento.capacidade):
                raise ValueError("O evento já está lotado.")

            participante = self.controlador_sistema.controlador_participante.selecionar()

            if(participante.nascimento > evento.data):
                raise ValidationException(
                    "O participante escolhido nasceu após o evento ser realizado.")

            if(participante.cpf not in cpfs):
                evento.adicionar_participante(participante)
                self.tela.mostrar_mensagem("Participante incluído!")
                self.dao.persist(evento)
            else:
                raise ValidationException(
                    "Participante já registrado no evento.")
        except CancelOperationException as err:
            self.tela.mostrar_mensagem(err)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def remover_participante(self, evento, input):
        try:
            participantes_registrados = evento.get_all_participantes()

            index = input["row_index"][0]

            participante = participantes_registrados[index]

            evento.remover_participante(participante)

            for registro in evento.registros_de_presenca:
                if registro.participante == participante:
                    evento.remover_registro_de_presenca(registro)

            self.dao.persist(evento)
            self.tela.mostrar_mensagem("Participante removido!")

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def confirmar_participante(self, evento, input, modo):
        try:
            # exibe participantes não confirmados
            # pede seleção de um participante

            index = input["row_index"][0]

            participante = evento.participantes_a_confirmar[index]

            if(modo):
                confirmacao = participante.cartao_de_vacina.is_complete()
            else:
                confirmacao = self.confirmar_com_exame(
                    evento.data, participante.exames)

            if(confirmacao):
                # remove participante da lista de a confirmar
                # inclui na lista de participantes confirmados
                evento.confirmar_participante(participante)
                self.dao.persist(evento)
                self.tela.mostrar_mensagem("Participante confirmado!")
            else:
                raise ValidationException(
                    "Participante não completou os requisitos para confirmação")

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def confirmar_com_exame(self, data_evento, exames):

        exame = self.controlador_sistema.controlador_exame.selecionar(exames)

        prazo = data_evento - exame.data
        if(exame.data <= data_evento and not exame.resultado and prazo <= timedelta(days=3)):
            return True

        return False

    def listar_organizadores(self, evento):

        try:
            return self.controlador_sistema.controlador_organizador.listar(
                evento.organizadores)

        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def adicionar_organizador(self, evento):
        try:
            organizador = self.controlador_sistema.controlador_organizador.selecionar()
            cpfs = [organizador.cpf for organizador in evento.organizadores]

            if(organizador.cpf in cpfs):
                raise ValidationException(
                    "Organizador já registrado no evento.")

            if(organizador.nascimento > evento.data):
                raise ValidationException(
                    "O organizador escolhido nasceu após o evento ser realizado.")

            evento.adicionar_organizador(organizador)
            self.dao.persist(evento)
            self.tela.mostrar_mensagem("Organizador incluído!")
        except CancelOperationException as err:
            self.tela.mostrar_mensagem(err)
        except ValidationException as err:
            self.tela.mostrar_mensagem(err)

    def remover_organizador(self, evento, input):
        try:

            index = input["row_index"][0]

            if(len(evento.organizadores) == 1):
                raise ValidationException(
                    "Evento possui apenas um organizador. É necessário adicionar outro organizador antes de removê-lo.")

            organizador = evento.organizadores[index]

            evento.remover_organizador(organizador)
            self.dao.persist(evento)
            self.tela.mostrar_mensagem("Organizador removido!")
        except ValidationException as err:
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
                    raise ValidationException(
                        "Participante já possui registro de entrada.")

            # Sistema solicita o horário da entrada.

            entrada = self.tela.mostrar_tela_registrar_presenca(
                evento.data, delta_limit)

            # Sistema cria o registro de presença e insere no evento
            registro = RegistroDePresenca(participante, entrada["data"])
            evento.adicionar_registro_de_presenca(registro)
            self.dao.persist(evento)

        except CancelOperationException as err:
            self.tela.mostrar_mensagem(err)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def registrar_saida(self, evento, input):

        # na lista de participantes, o usuário seleciona a opção registrar saída
        # Não havendo registros de presença, exibe mensagem de que ainda não foram registradas entrada
        # Sistema lista os registros de entrada já cadastrados
        # Sistema solicita a seleção de um paritipante para registrar a saída
        # Sistema solicita o horário da saída
        # SIstema insere a saída no registro

        delta_limit = timedelta(days=1)
        index = input["row_index"][0]

        try:

            if(len(evento.registros_de_presenca) == 0):
                raise ValueError(
                    "Ainda não foi registrada a entrada de nenhum participante")

            registro = evento.registros_de_presenca[index]

            if(registro.saida is not None):
                raise ValidationException(
                    "A saída deste participante já foi registrada")

            saida = self.tela.mostrar_tela_registrar_presenca(
                evento.data, delta_limit)

            registro.saida = saida["data"]
            self.dao.persist(evento)

        except CancelOperationException as err:
            self.tela.mostrar_mensagem(err)
        except ValueError as err:
            self.tela.mostrar_mensagem(err)

    def alterar_registro_de_presenca(self, evento, input):

        try:
            delta_limit = timedelta(days=1)

            index = input["row_index"][0]
            registro = evento.registros_de_presenca[index]

            self.tela.mostrar_mensagem(
                "Informe a nova entrada", "Alterar entrada")

            entrada_antiga = {
                "data": registro.entrada.data.strftime("%d/%m/%Y"),
                "horario": registro.entrada.data.strftime("%H:%M")
            }

            entrada = self.tela.mostrar_tela_registrar_presenca(
                evento.data, delta_limit, entrada_antiga)
            registro.entrada = entrada["data"]

            if(registro.saida is not None):

                self.tela.mostrar_mensagem(
                    "Informe a nova saída", "Alterar saída")

                saida_antiga = {
                    "data": registro.saida.data.strftime("%d/%m/%Y"),
                    "horario": registro.saida.data.strftime("%H:%M")
                }

                saida = self.tela.mostrar_tela_registrar_presenca(
                    evento.data, delta_limit, saida_antiga)

                registro.saida = saida["data"]

            self.dao.persist(evento)
        except CancelOperationException as err:
            self.tela.mostrar_mensagem(err)

    def remover_registro_de_presenca(self, evento, input):

        index = input["row_index"][0]
        registro = evento.registros_de_presenca[index]

        confirmacao = self.tela.confirmar()
        if(confirmacao):
            evento.remover_registro_de_presenca(registro)
            self.dao.persist(evento)

    def atualizar_pessoa(self, pessoa):
        self.dao.update_pessoa(pessoa)

    def unpack(self, evento):

        return {
            "titulo": evento.titulo,
            "data": evento.data.strftime("%d/%m/%Y"),
            "horario": evento.data.strftime("%H:%M"),
            "cep": evento.local.cep,
            "rua": evento.local.rua,
            "numero": evento.local.numero,
            "bairro": evento.local.bairro,
            "cidade": evento.local.cidade,
            "estado": evento.local.estado,
            "capacidade": evento.capacidade,
            "participantes_total": len(evento.get_all_participantes())
        }

    def unpack_registro(self, registro):

        return {
            "participante": registro.participante.nome,
            "entrada": registro.entrada.data.strftime("%d/%m/%Y %H:%M"),
            "saida": registro.saida.data.strftime("%d/%m/%Y %H:%M") if registro.saida else ""
        }
