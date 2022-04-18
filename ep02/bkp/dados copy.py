aeroportos = {
    'VCP': 0,  # São Paulo Viracopos
    'CGH': 5,  # São Paulo Congonhas
    'GRU': 6,  # São Paulo Guarulhos Cumbica
    'SDU': 10,  # Rio De Janeiro Santos Dumont
    'GIG': 11,  # Rio de Janeiro Galeão Internacional
    'CNF': 15,  # Belo Horizonte Confins Tancredo Neves
    'CGB': 20,  # Cuiabá
    'GYN': 21,  # Goiânia
    'CGR': 22,  # Campo Grande
    'POA': 30,  # Porto Alegre
    'SSA': 30,  # Salvador
    'BEL': 35,  # Belém
    'AJU': 36,  # Aracaju
    'BSB': 15,  # Brasília
    'REC': 40,  # Recife
    'MCZ': 10,  # Maceió
    'CWB': 40,  # Curitiba Afonso Pena
    'FOR': 45,  # Fortaleza
    'MAO': 50,  # Manaus
    'NAT': 45,  # Natal
    'FLN': 45  # Florianópolis
}

companias = {
    'AV': {'aeroportos': ['VCP', 'CGH', 'GRU', 'SDU'], 'nome': 'Avianca Brasil'},
    'AD': {'aeroportos': ['VCP', 'GRU', 'SDU'], 'nome': 'Azul Linhas Aéreas'},
    'G3': {'aeroportos': ['VCP', 'GRU', 'SDU', 'GIG'], 'nome': 'Gol Transportes Aéreos'},
    'P8': {'aeroportos': ['VCP', 'CGH', 'SDU'], 'nome': 'Pantanal Linhas Aéreas'},
    'Y8': {'aeroportos': ['VCP', 'CGH', 'SDU'], 'nome': 'Passaredo'},
    'JJ': {'aeroportos': ['VCP', 'CGH', 'GRU', 'SDU', 'GIG'], 'nome': 'TAM Linhas Aéreas'},
    'T4': {'aeroportos': ['VCP', 'CGH', 'SDU'], 'nome': 'TRIP Linhas Aereas'},
    'WH': {'aeroportos': ['VCP', 'CGH', 'SDU'], 'nome': 'WebJet Linhas Aéreas'}
}

# Testes
if __name__ == '__main__':
    import random
    from aviao import Aviao

    for compania in companias:
        print(companias[compania]['nome'], companias[compania]['aeroportos'])

    for aeroporto in aeroportos:
        print(aeroporto, aeroportos[aeroporto])

    print(random.choice(list(companias.keys())))
    id, value = random.choice(list(companias.items()))
    print(id, value['aeroportos'], value['nome'])
    print(id, value['aeroportos'], value['nome'])

    aviao = Aviao(
        min_combustivel_aviao = 1,
        max_combustivel_aviao = 10,
        min_duracao_voo = 1,
        max_duracao_voo = 50
    )
    print(aviao.aeroporto, random.choice(list(aeroportos.keys())))
    print(random.choices(['Regular', 'Emergencia'], weights=(85, 15), k=1)[0])
    print(f'{aviao.situacao}: Aeronave {aviao.id} pronto para {aviao.intencao} para aeroporto {aviao.aeroporto}, duracao do voo: {aviao.duracao_voo}')

