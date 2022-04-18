from simulacao_aeroporto import SimulacaoAeroporto

# Configuração
config = dict(
                MAX_AVIOES = 5,
                MAX_AEROPORTOS = 20,
                MAX_DURACAO_VOO = 50,
                MIN_DURACAO_VOO = 1,
                MAX_PERC_ESPERA_DECOLAGEM = 0.1,
                MAX_VOOS_SITUACAO_CRITICA = 4,
                MAX_PERC_VOOS_EMERGENCIA = 0.15,
                MAX_COMBUSTIVEL_AVIAO = 10,
                MIN_COMBUSTIVEL_AVIAO = 1,
                PISTAS_DECOLAGEM = [3],
                PISTAS_POUSO = [1, 2],
                MAX_TEMPO_SIMULACAO = 121, # Qde de ciclos da simulação
                DURACAO_CICLO = 1 # Duração mínima de cada ciclo em segundos
        )

if __name__ == '__main__':
    '''
    Cria e inicia a simulação
    '''
    aeroporto = SimulacaoAeroporto(**config)
    aeroporto.inicia()