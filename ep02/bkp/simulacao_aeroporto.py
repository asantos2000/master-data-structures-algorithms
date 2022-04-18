import time
import random
from aviao import Aviao
from dados import aeroportos
import logging
import heapq as hq

# Logging
logging.basicConfig(filename='simulacao_aeroporto.log',
                    encoding='utf-8',
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class SimulacaoAeroporto:
    def __init__(self, **kwargs):
        config = kwargs
        # Configuração da simulação
        self.max_avioes = config.get('MAX_AVIOES')
        self.max_aeroportos = config.get('MAX_AEROPORTOS')
        self.max_duracao_voo = config.get('MAX_DURACAO_VOO')
        self.min_duracao_voo = config.get('MIN_DURACAO_VOO')
        self.max_perc_espera_decolagem = config.get('MAX_PERC_ESPERA_DECOLAGEM')
        self.max_voos_situacao_critica = config.get('MAX_VOOS_SITUACAO_CRITICA')
        self.min_duracao_voo = config.get('MIN_DURACAO_VOO')
        self.max_perc_voos_emergencia = config.get('MAX_PERC_VOOS_EMERGENCIA')
        self.max_combustivel_aviao = config.get('MAX_COMBUSTIVEL_AVIAO')
        self.min_combustivel_aviao = config.get('MIN_COMBUSTIVEL_AVIAO')
        self.qde_combustivel_aviao_espera_pouso = 0
        self.num_pistas = config.get('NUM_PISTAS')
        self.max_tempo_simulacao = config.get('MAX_TEMPO_SIMULACAO')
        self.tempo_simulacao = 0
        self.duracao_ciclo = config.get('DURACAO_CICLO')
        self.aeroportos = aeroportos
        self.fila_pouso = []
        self.fila_decolar = []
        self.pistas = []
        self.qde_avioes_pistas = []
        for _ in range(self.num_pistas):
            self.pistas.append([])
            self.qde_avioes_pistas.append(0)
        # Variáveis da simulação
        self.qde_avioes_fila_pouso = 0
        self.qde_avioes_fila_decolar = 0
        self.tempo_medio_espera_decolagem = 0
        self.tempo_medio_espera_pouso = 0
        self.qde_media_combustivel_avioes_esperam_pouso = 0
        self.qde_media_combustivel_avioes_pousaram = 0 # TODO: Verificar como calcular
        self.qde_combustivel = 0 # TODO: Verificar se é necessário
        self.qde_avioes_pousaram = 0
        self.qde_avioes_emergencia = 0


    def imprime_logo(self):
        print('           __|__    ')
        print('__|__   *---(_)---* ')
        print('\___/               ')
        print(' | |   Tráfego Aéreo')
        print('_|_|_____.________  ')
        print('       / | \        ')
        print('      /  |  \       ')
        print('     /   |   \      ')

    def lista_aeroportos(self):
        return self.aeroportos

    def adiciona_aviao_fila_pouso(self, aviao):
        # Adiciona avião à fila de pouso
        chave = aviao.combustivel + self.tempo_simulacao
        hq.heappush(self.fila_pouso, chave, self.tempo_simulacao, aviao)

    def adiciona_aviao_fila_decolar(self, aviao):
        # Adiciona aviao a fila de decolagem
        self.fila_decolar.append(aviao)
        chave = aviao.tempo_espera + self.tempo_simulacao
        hq.heappush(self.fila_decolar, chave, self.tempo_simulacao, aviao)

    def comunicado_aviao(self, tempo=0):
        # Criação dos aviões
        aviao = Aviao(
            min_combustivel_aviao=self.min_combustivel_aviao,
            max_combustivel_aviao=self.max_combustivel_aviao,
            min_duracao_voo=self.min_duracao_voo,
            max_duracao_voo=self.max_duracao_voo,
            tempo_espera=0,
            tempo_decolagem=0,
            tempo_pouso=0,
            tempo_voo=0,
            tempo_pouso_decolagem=0,
            tempo_voo_decolagem=0,
            tempo_pouso_pouso=0,
            tempo_voo_pouso=0,
            tempo_voo_espera=0,
            tempo_voo_critico=0,
            tempo_voo_emergencia=0,
            tempo_voo_total=0,
            tempo_pouso_total=0,
            tempo_decolagem_total=0,
            tempo_espera_total=0,
            tempo_critico_total=0
        )
        return aviao

    def comunica_torre(self):
        '''
        Avioes comunicam intenção de pousar ou decolar
        '''
        for _ in range(random.randint(0, self.max_avioes)):
            # Simula tráfego - Gera dados para simulação
            aviao = self.comunicado_aviao(tempo=self.tempo_simulacao)

            if aviao.intencao == 'Decolar':
                logger.debug(
                    f'Ciclo: {self.tempo_simulacao}: {aviao.situacao}: Aeronave {aviao.id} pronto para {aviao.intencao} para aeroporto {aviao.aeroporto}, duracao do voo: {aviao.duracao_voo}')
                # Adiciona a fila de decolagem
                self.adiciona_aviao_fila_decolar(aviao)
            else:
                logger.debug(f'Ciclo: {self.tempo_simulacao}: {aviao.situacao}: Aeronave {aviao.id} proveniente de {aviao.aeroporto}, solicita {aviao.intencao} - Combustivel: {aviao.combustivel}, aeroportos permitidos para pouso: {aviao.aeroportos_chegada}')
                # Adiciona a fila de pouso
                self.adiciona_aviao_fila_pouso(aviao)

    def pista_menos_ocupada(self):
        return self.pistas.index(min(self.pistas))

    def autoriza_emergencia(self, aviao):
        if aviao.situacao == 'Emergencia' and aviao.intencao == 'Pousar':
            pista = self.pista_menos_ocupada()
            aviao.pista = pista
            self.adiciona_aviao_fila_pouso(aviao)
        if aviao.situacao == 'Emergencia' and aviao.intencao == 'Decolar':
            pista = self.pista_menos_ocupada()
            aviao.pista = pista
            self.adiciona_aviao_fila_decolar(aviao)

    def autoriza_pouso(self):
        pass

    def autoriza_decolagem(self):
        pass

    def decolar(self):
        pass

    def pousar(self):
        pass

    def atualiza_simulacao(self):
        '''
        Atualiza variáveis da simulação
        '''
        # Reinicia contadores
        self.qde_avioes_emergencia = 0
        self.qde_combustivel_aviao_espera_pouso = 0
        # Atualizações de pouso
        for aviao in self.fila_pouso:
            # Atualiza avioes
            aviao.combustivel -= 1 if aviao.combustivel > 0 else 0
            aviao.tempo_espera += 1
            aviao.tempo_pouso += 1
            if aviao.combustivel == 0:
                aviao.situacao = 'Emergencia'
            # Atualiza estatísticas emergência
            if aviao.situacao in 'Emergencia':
                self.qde_avioes_emergencia += 1
            # Atualiza estatísticas de combustível em espera
            self.qde_combustivel_aviao_espera_pouso += aviao.combustivel

        # Atualizações de decolagem
        tempo_total_espera = 0
        for aviao in self.fila_decolar:
            # Atualiza avioes
            aviao.tempo_espera += 1
            aviao.tempo_decolagem += 1
            if aviao.tempo_espera > aviao.tempo_voo * self.max_perc_espera_decolagem:
                aviao.situacao = 'Emergencia'

            # Atualiza estatísticas emergência
            if aviao.situacao in 'Emergencia':
                self.qde_avioes_emergencia += 1

            tempo_total_espera += aviao.tempo_espera

        # Atualiza qde avioes nas pistas
        for i, pista in enumerate(self.pistas):
            self.qde_avioes_pistas[i] = len(pista)

        # Atualiza estatísticas
        # Pouso
        self.qde_avioes_fila_pouso = len(self.fila_pouso)
        self.tempo_medio_espera_pouso = self.tempo_simulacao / \
            self.qde_avioes_fila_pouso if self.qde_avioes_fila_pouso else 0
        self.qde_media_combustivel_avioes_esperam_pouso = self.qde_combustivel_aviao_espera_pouso / \
            self.qde_avioes_fila_pouso if self.qde_avioes_fila_pouso else 0
        # Decolagem
        self.qde_avioes_fila_decolar = len(self.fila_decolar)
        self.qde_avioes_fila_decolar = self.qde_avioes_fila_decolar
        self.qde_media_combustivel_avioes_pousaram = self.qde_combustivel / \
            self.qde_avioes_pousaram if self.qde_avioes_pousaram else 0
        # Atualiza tempo medio de espera
        self.tempo_medio_espera_decolagem = tempo_total_espera / \
            self.qde_avioes_fila_decolar if self.qde_avioes_fila_decolar else 0

    def imprime_estatisticas(self):
        self.imprime_logo()
        print(f'Ciclo {self.tempo_simulacao}')
        # fila de pouso
        print('\n    🛬 Estatísticas de pouso')
        #print(f'        fila pouso: {self.fila_pouso}')
        print(f'        qde_avioes_fila_pouso: {self.qde_avioes_fila_pouso}')
        print(f'        tempo_medio_espera_pouso: {self.tempo_medio_espera_pouso:.2f}')
        print(f'        qde_combustivel_aviao_espera_pouso: {self.qde_combustivel_aviao_espera_pouso}')
        print(f'        qde_media_combustivel_avioes_esperam_pouso: {self.qde_media_combustivel_avioes_esperam_pouso:.2f}')
        print(f'        qde_media_combustivel_avioes_pousaram: {self.qde_media_combustivel_avioes_pousaram:.2f}')
        # fila de decolagem
        print('\n    🛫 Estatísticas de decolagem')
        #print(f'        fila decolagem: {self.fila_decolar}')
        print(f'        qde_avioes_fila_decolar: {self.qde_avioes_fila_decolar}')
        print(f'        tempo_medio_espera_decolagem: {self.tempo_medio_espera_decolagem:.2f}')
        # pistas
        print('\n    Pistas')
        # Imprime pistas
        for pista in self.pistas:
            print(f'        pista {pista}')
        print('\n    Estatisticas emergência')
        print(f'        qde_avioes_emergencia: {self.qde_avioes_emergencia}')

    def aguarda_tempo_ciclo(self):
        time.sleep(self.duracao_ciclo)

    # Laço principal da simulação
    def inicia(self):
        # Tempo de simulação
        for self.tempo_simulacao in range(self.max_tempo_simulacao):
            # Avioes comunicam com a torre
            self.comunica_torre()

            # Pousos
            # Autoriza pouso
            self.autoriza_pouso()

            # Decolagens
            # Autoriza decolagem
            self.autoriza_decolagem()

            # Estatísticas
            # Imprime estatísticas
            self.imprime_estatisticas()

            # Atualiza tempo da simulação
            self.atualiza_simulacao()

            # Aguarda duração mínima do ciclo
            self.aguarda_tempo_ciclo()
