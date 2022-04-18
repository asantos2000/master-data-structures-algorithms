import random
from dados import companias, aeroportos

class Aviao:
    '''
    Simula avião
    '''
    def __init__(self, **kwargs):
        config = kwargs
        id, values = random.choice(list(companias.items()))
        self.id = id + str(random.randint(100, 999))
        # Aeroportos que podem pousar
        self.aeroportos_chegada = values['aeroportos']
        self.aeroporto = random.choice(list(aeroportos.keys()))
        self.combustivel = random.randint(config.get('min_combustivel_aviao'), config.get('max_combustivel_aviao'))
        self.duracao_voo = random.randint(config.get('min_duracao_voo'), config.get('max_duracao_voo'))
        self.intencao = random.choice(['Pousar', 'Decolar'])
        self.situacao = random.choices(['Regular', 'Emergencia'], weights=(85, 15), k=1)[0]
