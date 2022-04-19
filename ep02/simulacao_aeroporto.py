import time
import random
from aviao import Aviao
from dados import aeroportos
from sim_logger import logger_data, logger_com
# Fila de prioridade - default heap de minimo
import heapq as hq

# Constantes
PRIORIDADE_MAXIMA = -1

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
        self.pistas_decolagem = config.get('PISTAS_DECOLAGEM')
        self.pistas_pouso = config.get('PISTAS_POUSO')
        self.max_tempo_simulacao = config.get('MAX_TEMPO_SIMULACAO')
        self.tempo_simulacao = 0
        self.duracao_ciclo = config.get('DURACAO_CICLO')
        self.aeroportos = aeroportos
        self.fila_pouso = []
        self.fila_decolar = []
        # Variáveis de estado da simulação
        self.qde_avioes_fila_pouso = 0
        self.qde_avioes_fila_decolar = 0
        self.qde_combustivel_avioes_pousaram = 0
        self.qde_avioes_pousaram = 0
        self.qde_avioes_decolaram = 0
        self.total_tempo_avioes_esperam_decolagem = 0
        self.total_combustivel_avioes_esperam_pouso = 0
        self.total_tempo_avioes_esperam_pouso = 0
        self.total_tempo_avioes_esperaram_pouso = 0
        self.qde_avioes_crash = 0
        # Indicadores
        self.tempo_medio_espera_decolagem = 0
        self.tempo_medio_espera_pouso = 0
        self.qde_media_combustivel_avioes_esperam_pouso = 0
        self.qde_media_combustivel_disponivel_avioes_pousaram = 0
        self.qde_avioes_pousando_emergencia = 0
        self.qde_avioes_decolando_emergencia = 0

    def imprime_logo(self):
        '''
        Imprime o logo da simulação
        '''
        fb = random.choice('_o')
        lights1 = random.choice('*-')
        lights2 = random.choice('* ')
        print(f'  {lights2}        __|__    ')
        print(f'__|__   {lights1}---({fb})---{lights1} ')
        print('\___/               ')
        print(' | |   Tráfego Aéreo')
        print('_|_|_____.________  ')
        print('       / | \        ')
        print('      /  |  \       ')
        print('     /   |   \      ')

    def adiciona_aviao_fila_pouso(self, aviao):
        '''
        Adiciona aviao a fila de pouso priorizando emergências
        '''
        # Adiciona avião à fila de pouso
        # Se situacao de emergencia prioridade máxima
        if aviao.situacao == 'Emergencia':
            chave = PRIORIDADE_MAXIMA
            self.qde_avioes_pousando_emergencia += 1
        else:
            # Considerando que o combustivel decrementa uma unidade a cada segundo.
            # Adicionar o tempo do ciclo ao combustivel permite manter
            # a prioridade sem a necessidade de reordenar a fila
            chave = (aviao.combustivel + self.tempo_simulacao)
        # Conteúdo da fila: (prioridade, tempo da simulação qdo avião entrou na fila, aviao)
        hq.heappush(self.fila_pouso, (chave, id(aviao), self.tempo_simulacao, aviao))
        self.total_combustivel_avioes_esperam_pouso += aviao.combustivel
        # Dados da simulação
        logger_data.info(f';push_pouso;{self.tempo_simulacao};{self.tempo_simulacao};{chave};{aviao.id};{aviao.combustivel};{aviao.situacao};{aviao.duracao_voo}')
        # Dados de comunicação
        logger_com.info(f't: {self.tempo_simulacao}: Torre - Aeronave {aviao.id} aguarde pouso circulando aeroporto')

    def adiciona_aviao_fila_decolar(self, aviao):
        '''
        Adiciona aviao a fila de decolagem priorizando emergências
        '''
        # Adiciona aviao a fila de decolagem
        # A prioridade é um percentual da duracao do voo (tempo máximo de espera na fila)
        # somado ao ciclo da simulação para evitar reordenar a fila.
        if aviao.situacao == 'Emergencia':
            chave = PRIORIDADE_MAXIMA
            self.qde_avioes_decolando_emergencia += 1
        else:
            chave = (aviao.duracao_voo * self.max_perc_espera_decolagem) + self.tempo_simulacao
        hq.heappush(self.fila_decolar, (chave, id(aviao), self.tempo_simulacao, aviao))
        # Dados da simulação
        logger_data.info(f';push_decolar;{self.tempo_simulacao};{self.tempo_simulacao};{chave};{aviao.id};{aviao.combustivel};{aviao.situacao};{aviao.duracao_voo}')
        # Dados de comunicação
        logger_com.info(f't: {self.tempo_simulacao}: Torre - Aeronave {aviao.id} entre na fila de decolagem')

    def simula_trafego(self):
        '''
        Simula o tráfego aéreo
        '''
        # Criação dos aviões
        return Aviao(
            min_combustivel_aviao=self.min_combustivel_aviao,
            max_combustivel_aviao=self.max_combustivel_aviao,
            min_duracao_voo=self.min_duracao_voo,
            max_duracao_voo=self.max_duracao_voo
        )

    def comunica_torre(self):
        '''
        Avioes comunicam intenção de pousar ou decolar
        '''
        for _ in range(random.randint(0, self.max_avioes)):
            # Simula tráfego - Gera dados para simulação
            aviao = self.simula_trafego()

            if aviao.intencao == 'Decolar':
                # Adiciona a fila de decolagem
                self.adiciona_aviao_fila_decolar(aviao)
                # Dados de comunicação
                logger_com.info(f't: {self.tempo_simulacao}: Aeronave - {aviao.id}, situação {aviao.situacao}, pronto para {aviao.intencao} para aeroporto {aviao.aeroporto}, duracao do voo: {aviao.duracao_voo}')
            else:
                # Adiciona a fila de pouso
                self.adiciona_aviao_fila_pouso(aviao)
                # Dados de comunicação
                logger_com.info(f't: {self.tempo_simulacao}: Aeronave - {aviao.id}, situação {aviao.situacao}, proveniente de {aviao.aeroporto}, solicita {aviao.intencao} - Combustivel: {aviao.combustivel}, aeroportos permitidos para pouso: {aviao.aeroportos_chegada}')

    def pousar(self):
        '''
        Pousa aviões
        Retira aviões da fila de pouso
        '''
        # Verifica se há aviões na fila de pouso
        for p in self.pistas_pouso:
            if self.fila_pouso:
                chave, id_obj, t_entrada_fila , aviao = hq.heappop(self.fila_pouso)
                tempo_decorrido = (self.tempo_simulacao - t_entrada_fila)
                combustivel_restante = aviao.combustivel - tempo_decorrido
                self.total_tempo_avioes_esperaram_pouso += tempo_decorrido
                self.total_combustivel_avioes_esperam_pouso -= aviao.combustivel
                self.qde_combustivel_avioes_pousaram += combustivel_restante
                self.qde_avioes_pousaram += 1
                # Emergencia                    
                if (aviao.combustivel - tempo_decorrido) == 0:
                    self.qde_avioes_pousando_emergencia += 1
                if (aviao.combustivel - tempo_decorrido) < 0:
                    self.qde_avioes_crash += 1
                # Dado de simulação
                logger_data.info(f';pop_pouso;{self.tempo_simulacao};{t_entrada_fila};{chave};{aviao.id};{aviao.combustivel};{aviao.situacao};{aviao.duracao_voo}')
                # Dado de comunicação
                logger_com.info(f't: {self.tempo_simulacao}: Torre - {aviao.id}, situação {aviao.situacao} pousar pista {p}')

    def pouso_emergencia(self):
        '''
        Pouso de emergencia
        Desvia avião para fila de decolagem
        para usar a pista para pouso
        '''
        # Pouso emergencia nas pistas de decolagem
        if len(self.fila_pouso) > 0:
            chave, id_obj, t_entrada_fila , aviao = self.fila_pouso[0]
            if aviao.situacao == 'Emergencia':
                chave = PRIORIDADE_MAXIMA
                hq.heappush(self.fila_decolagem, (chave, id_obj, t_entrada_fila, aviao))
                # Dado de simulação
                logger_data.info(f';pop_pouso;{self.tempo_simulacao};{t_entrada_fila};{chave};{aviao.id};{aviao.combustivel};{aviao.situacao};{aviao.duracao_voo}')
                # Dado de comunicação
                logger_com.info(f't: {self.tempo_simulacao}: Torre - aeronave {aviao.id}, situação {aviao.situacao} autorizando uso da pista de decolagem para pouso')

    def desvia_aviao_outro_aeroporto(self):  # sourcery skip: last-if-guard
        '''
        Desvia avião para outro aeroporto
        Se próxima iteração avião em risco de crash,
        desvia para outro aeroporto
        '''
        if len(self.fila_pouso) > 0:
            for blip in hq.nsmallest(self.max_voos_situacao_critica, self.fila_pouso):
                _, _, _, aviao = blip
                # Quantidade de avioes na fila de pouso dividido pela qde de pistas mais um ciclo
                tempo_estimado_para_pouso = (len(self.fila_pouso) // len(self.pistas_pouso)) + 1
                # Assume uma unidade de combustivel para uma unidade de tempo
                if aviao.combustivel < tempo_estimado_para_pouso:
                    # Primeiro sempre o aeroporto corrente
                    # Busca o próximo aeroporto
                    aeroporto_para_pouso = next(iter(aviao.aeroportos_chegada[1:]))
                    distancia_proximo_aeroporto = aeroportos[aeroporto_para_pouso]
                    if distancia_proximo_aeroporto <= aviao.combustivel:
                        # Tira o avião da fila de pouso
                        chave, _, _, aviao = hq.heappop(self.fila_pouso)
                        self.total_combustivel_avioes_esperam_pouso -= aviao.combustivel
                        # Dado de simulação
                        logger_data.info(f';pop_desvia;{self.tempo_simulacao};{self.tempo_simulacao};{chave};{aviao.id};{aviao.combustivel};{aviao.situacao};{aviao.duracao_voo}')
                        # Dado de comunicação
                        logger_com.info(f't: {self.tempo_simulacao}: Torre - {aviao.id}, situação {aviao.situacao} proceder para {aeroporto_para_pouso}, distância {distancia_proximo_aeroporto}')
                    else:
                        # Mantém avião na fila de pouso
                        # Dado de comunicação
                        logger_com.info(f't: {self.tempo_simulacao}: Torre - {aviao.id}, situação {aviao.situacao} permanecer na fila de pouso')

    def decolar(self):
        '''
        Decola aviões
        Retira aviões da fila de decolagem
        '''
        for p in self.pistas_decolagem:
            if self.fila_decolar:
                chave, id_obj, t_entrada_fila , aviao = hq.heappop(self.fila_decolar)
                tempo_decorrido = (self.tempo_simulacao - t_entrada_fila)
                self.total_tempo_avioes_esperam_decolagem += tempo_decorrido
                self.qde_avioes_decolaram += 1
                # Se aviao usou a pista para pousar
                if aviao.intencao == 'Pousar':
                    self.total_combustivel_avioes_esperam_pouso -= aviao.combustivel
                    self.qde_avioes_pousaram += 1
                    # Dado de simulação
                    logger_data.info(f';pop_pouso;{self.tempo_simulacao};{t_entrada_fila};{chave};{aviao.id};{aviao.combustivel};{aviao.situacao};{aviao.duracao_voo}')
                    # Dado de comunicação
                    logger_com.info(f't: {self.tempo_simulacao}: Torre - aeronave {aviao.id}, situação {aviao.situacao} pousar pista {p}')
                # Emergencia
                if (aviao.duracao_voo * self.max_perc_espera_decolagem) > tempo_decorrido:
                    self.qde_avioes_decolando_emergencia += 1
                    # Dado de comunicação
                    logger_com.info(f't: {self.tempo_simulacao}: Torre - aeronave {aviao.id}, autorizando decolagem com prioridade tempo de espera {tempo_decorrido}')
                # Dado de simulação
                logger_data.info(f';pop_decolar;{self.tempo_simulacao};{t_entrada_fila};{chave};{aviao.id};{aviao.combustivel};{aviao.situacao};{aviao.duracao_voo}')
                # Dado de comunicação
                logger_com.info(f't: {self.tempo_simulacao}: Torre - {aviao.id}, situação {aviao.situacao} decolar pista {p}')

    def atualiza_simulacao(self):
        '''
        Atualiza variáveis da simulação
        '''
        # Atualiza estatísticas
        # Pouso
        self.qde_avioes_fila_pouso = len(self.fila_pouso)
        self.tempo_medio_espera_pouso = self.total_tempo_avioes_esperaram_pouso / \
            self.qde_avioes_pousaram if self.qde_avioes_pousaram else 0
        self.qde_media_combustivel_avioes_esperam_pouso = self.total_combustivel_avioes_esperam_pouso / \
            self.qde_avioes_fila_pouso if self.qde_avioes_fila_pouso else 0
        self.qde_media_combustivel_disponivel_avioes_pousaram = self.qde_combustivel_avioes_pousaram / \
            self.qde_avioes_pousaram if self.qde_avioes_pousaram else 0

        # Decolagem
        # Atualiza tempo medio de espera
        self.qde_avioes_fila_decolar = len(self.fila_decolar)
        self.tempo_medio_espera_decolagem = self.total_tempo_avioes_esperam_decolagem / \
            self.qde_avioes_decolaram if self.qde_avioes_decolaram else 0

    def imprime_estatisticas(self):
        '''
        Imprime estatísticas da simulação
        '''
        self.imprime_logo()
        print(f'\n🔂 Ciclo {self.tempo_simulacao}')
        # fila de pouso
        print('\n    🛬 Estatísticas de pouso')
        print(f'        fila pouso: {[aviao.id for _, _, _, aviao in self.fila_pouso]}')
        print(f'        qde_avioes_fila_pouso: {len(self.fila_pouso)}')
        print(f'        qde_avioes_pousaram: {self.qde_avioes_pousaram}')
        print(f'        tempo_medio_espera_pouso: {self.tempo_medio_espera_pouso:.2f}')
        print(f'        qde_media_combustivel_avioes_esperam_pouso: {self.qde_media_combustivel_avioes_esperam_pouso:.2f}')
        print(f'        qde_media_combustivel_disponivel_avioes_pousaram: {self.qde_media_combustivel_disponivel_avioes_pousaram:.2f}')
        # fila de decolagem
        print('\n    🛫 Estatísticas de decolagem')
        print(f'        fila decolagem: {[aviao.id for _, _, _, aviao in self.fila_decolar]}')
        print(f'        qde_avioes_fila_decolar: {len(self.fila_decolar)}')
        print(f'        tempo_medio_espera_decolagem: {self.tempo_medio_espera_decolagem:.2f}')
        print(f'        qde_avioes_decolaram: {self.qde_avioes_decolaram}')
        print('\n    🚨 Estatisticas de emergências')
        print(f'        qde_avioes_pousando_emergencia: {self.qde_avioes_pousando_emergencia}')
        print(f'        qde_avioes_decolando_emergencia: {self.qde_avioes_decolando_emergencia}')
        print(f'        qde_avioes_crash: {self.qde_avioes_crash}')

    def aguarda_tempo_ciclo(self):
        '''
        Reduz a velocidade da iteração criando uma duração mínima para cada ciclo
        '''
        time.sleep(self.duracao_ciclo)

    # Laço principal da simulação
    def inicia(self):
        '''
        Inicia a simulação
        '''
        # Tempo de simulação
        for self.tempo_simulacao in range(self.max_tempo_simulacao):
            # Avioes comunicam com a torre
            self.comunica_torre()

            # Decolar avioes
            self.decolar()

            # Pousar avioes
            self.pousar()

            # Pouso emergencia
            self.pouso_emergencia()

            # Verifica se próximo ciclo avião com 
            # problema e desvia outro aeroporto
            self.desvia_aviao_outro_aeroporto()

            # Estatísticas
            # Imprime estatísticas
            self.imprime_estatisticas()

            # Atualiza tempo da simulação
            self.atualiza_simulacao()

            # Aguarda duração mínima do ciclo
            self.aguarda_tempo_ciclo()

