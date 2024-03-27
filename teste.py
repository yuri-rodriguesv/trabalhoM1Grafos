from collections import deque

def fecho_transitivo_inverso(matriz_adjacencia):
    tamanho_grafo = len(matriz_adjacencia)
    fecho = [[0] * tamanho_grafo for _ in range(tamanho_grafo)]

    # Função para realizar uma busca em largura a partir de um vértice de destino
    def bfs(destino):
        visitados = [False] * tamanho_grafo
        fila = deque([destino])

        while fila:
            atual = fila.popleft()
            for vizinho in range(tamanho_grafo):
                if matriz_adjacencia[vizinho][atual] == 1 and not visitados[vizinho]:
                    visitados[vizinho] = True
                    fila.append(vizinho)
                    fecho[vizinho][destino] = 1

    # Executa a busca em largura a partir de cada vértice do grafo
    for vertice in range(tamanho_grafo):
        bfs(vertice)

    return fecho

# Grafo de exemplo fornecido
grafo_exemplo = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

# Calcula o fecho transitivo inverso do grafo exemplo
resultado_fecho_inverso = fecho_transitivo_inverso(grafo_exemplo)

# Exibe o resultado
print("Fecho Transitivo Inverso:")
for linha in resultado_fecho_inverso:
    print(linha)

