def color_nodes(graph):
    color_map = {}
    # Ordena vertices por grau em ordem descendent
    vertices = sorted(graph, key=lambda x: len(graph[x]), reverse=True)
    print(vertices)
    # Fila de prioridade
    for node in vertices:
        neighbor_colors = {color_map.get(neigh) for neigh in graph[node]}
        color_map[node] = next(
            # Escolha gulosa
            color for color in range(len(graph)) if color not in neighbor_colors
        )
    return color_map

if __name__ == '__main__':
  # graph = {
  #   'a': list('bcd'),
  #   'b': list('ac'),
  #   'c': list('abdef'),
  #   'd': list('ace'),
  #   'e': list('cdf'),
  #   'f': list('ce')
  # }

  # print(graph)
  # print(color_nodes(graph))

  graph = {
    'a': list('bcd'),
    'b': list('aei'),
    'c': list('agh'),
    'd': list('afj'),
    'e': list('bfh'),
    'f': list('deg'),
    'g': list('icf'),
    'h': list('jce'),
    'i': list('bgj'),
    'j': list('ihd')
  }

  print(graph)
  print(color_nodes(graph))