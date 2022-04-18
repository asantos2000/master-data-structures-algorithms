def arquivos_para_copia(arquivos, C):
    # C - capacidade do pendrive

    # arquivos_ordenados: ordene f e t de tal forma que
    # f[1]    f[2]
    # t[1] >= t[2] ... >= t[n]
    # arquivos = {f: t}
    arquivos_ordenados = dict(
        sorted(arquivos.items(), key=lambda item: item[1], reverse=True))
    s = 0   # indicador da solução encontrada
    p = []  # Lista de arquivos para copia
    i = 1
    n = len(arquivos)

    while i <= n and C > 0:
        arquivo = arquivos_ordenados.popitem()
        t = arquivo[1]
        f = arquivo[0]

        if t <= C:
            p.append(f)  # colocar arquivo na lista de arquivos para copia
            C = C - t
        else:
            break  # Arquivos restantes são maiores que a capacidade do pendrive

        i = i + 1

    if len(p) == 0:
        s = 0       # Não encontrou solução
    elif C > 0:
        s = 1       # Solução não ótima
    else:
        s = 2       # Solução ótima

    return p, s

# Código de teste
if __name__ == "__main__":
    # Otima
    arquivos = {1: 50,
                2: 10,
                3: 70,
                4: 10,
                5: 150,
                6: 120}
    print(arquivos_para_copia(arquivos, 140))

    # Não otima
    arquivos = {1: 70,
                2: 10,
                3: 70,
                4: 10,
                5: 150,
                6: 120}
    print(arquivos_para_copia(arquivos, 140))

    # Não encontrou solução
    arquivos = {1: 150,
                2: 200}
    print(arquivos_para_copia(arquivos, 140))
