# Simulação aeroporto

ver README.md ou README.pdf

## Executando a simulação

```bash
# Requer python 3+
python main.py
```

Em outro terminal execute:

```bash
# Log de comunicação entre a torre e a aeronave
tail -f simulacao-aeroporto-com.log
# Dados da simulação
# data; evento; tempo_simulacao; t_entrada_fila; chave; aviao.id; aviao.combustivel; aviao.situacao;aviao.duracao_voo
tail -f simulacao-aeroporto-data.log
```
