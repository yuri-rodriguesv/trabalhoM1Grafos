import os
from collections import deque

def limpar_tela():
  os.system('cls')  # Windows

def input_origem_fim(quantidadeVertices, opOrientacao, matriz, inserir):
    while True:
        try:
            verticeOrigem = int(input("Qual o vértice de origem: "))
            verticeFim = int(input("Qual o vértice fim: "))
            if verticeOrigem > quantidadeVertices or verticeFim > quantidadeVertices:
                raise ValueError(f"O numero maximo de vértices é de {quantidadeVertices}, por favor insira um valor válido!")
            elif verticeOrigem == verticeFim:
                raise ValueError("Os vértices de origem e fim não podem ser iguais.")
            break 
        except ValueError as e:
            print("Erro: ", e)
            input("Pressione qualquer tecla para continuar...")
            limpar_tela()

    if inserir == True:
        if opOrientacao == "n":
            matriz[verticeOrigem - 1][verticeFim - 1] = 1
            matriz[verticeFim - 1][verticeOrigem - 1] = 1
            print("Inserção feita com sucesso!")
            limpar_tela()
        else:
            matriz[verticeOrigem - 1][verticeFim - 1] = 1
            print("Inserção feita com sucesso!")
            limpar_tela()
    else:
        if opOrientacao == "n":
            matriz[verticeOrigem - 1][verticeFim - 1] = 0
            matriz[verticeFim - 1][verticeOrigem - 1] = 0
            print("Exclusão feita com sucesso!")
            limpar_tela()
        else:
            matriz[verticeOrigem - 1][verticeFim - 1] = 0
            print("Exclusão feita com sucesso!")
            limpar_tela()
    
def DFS(quantidadeVertices, matriz):
    pilha = []
    visitas = [0] * quantidadeVertices  # Inicializando a lista de visitas com zeros

    while True:
        try:
            verticeOrigem = int(input("Qual o vértice de origem: "))
            if verticeOrigem > quantidadeVertices:
                raise ValueError(f"O número máximo de vértices é de {quantidadeVertices}, por favor insira um valor válido!")
            break
        except ValueError as e:
            print("Erro: ", e)
            input("Pressione qualquer tecla para continuar...")
            limpar_tela()

    pilha.append(verticeOrigem)  # Adiciona o vértice de origem à pilha

    while pilha:
        verticeAtual = pilha.pop()
        if not visitas[verticeAtual - 1]:
            print(verticeAtual, end=" ")
            visitas[verticeAtual - 1] = 1  # Marca o vértice como visitado
            for i in range(quantidadeVertices - 1, -1, -1):  # Itera sobre os vértices adjacentes na ordem inversa
                if matriz[verticeAtual - 1][i] and not visitas[i]:  # Se há uma aresta e o vértice adjacente não foi visitado
                    pilha.append(i + 1)  # Adiciona o vértice adjacente à pilha

    print(visitas)  # Nova linha para melhorar a legibilidade da saída
   
def BFS(quantidadeVertices, matriz):

    fila = deque()  # Inicializa uma fila vazia
    visitas = [0] * quantidadeVertices  # Inicializa a lista de visitas com zeros

    while True:
        try:
            verticeOrigem = int(input("Qual o vértice de origem: "))
            if verticeOrigem > quantidadeVertices:
                raise ValueError(f"O número máximo de vértices é de {quantidadeVertices}, por favor insira um valor válido!")
            break
        except ValueError as e:
            print("Erro: ", e)
            input("Pressione qualquer tecla para continuar...")
            limpar_tela()

    fila.append(verticeOrigem)  # Adiciona o vértice de origem à fila
    visitas[verticeOrigem - 1] = 1  # Marca o vértice de origem como visitado

    while fila:
        verticeAtual = fila.popleft()  # Remove o primeiro elemento da fila
        print(verticeAtual, end=" ")

        for i in range(quantidadeVertices):
            if matriz[verticeAtual - 1][i] and not visitas[i]:
                fila.append(i + 1)  # Adiciona o vértice adjacente à fila
                visitas[i] = 1  # Marca o vértice adjacente como visitado

    print(visitas)  # Nova linha para melhorar a legibilidade da saída

def fecho_transitivo_direto(matriz_adjacencia, tipoBusca):
    tamanho_grafo = len(matriz_adjacencia)
    fecho = [[0] * tamanho_grafo for _ in range(tamanho_grafo)]

    if tipoBusca == True:
        def dfs(destino):
            visitados = [False] * tamanho_grafo
            pilha = [destino]

            while pilha:
                atual = pilha.pop()
                if not visitados[atual]:
                    visitados[atual] = True
                    for vizinho in range(tamanho_grafo):
                        if matriz_adjacencia[vizinho][atual] == 1 and not visitados[vizinho]:
                            pilha.append(vizinho)
                            fecho[vizinho][destino] = 1

        # Executa a busca em profundidade a partir de cada vértice do grafo
        for vertice in range(tamanho_grafo):
            dfs(vertice)
        return fecho
    else: 
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

def fecho_transitivo_inverso(matriz_adjacencia, tipoBusca):
    tamanho_grafo = len(matriz_adjacencia)
    fecho = [[0] * tamanho_grafo for _ in range(tamanho_grafo)]

    # Função para realizar uma busca em profundidade a partir de um vértice de destino
    if tipoBusca == True:
        def dfs(destino):
            visitados = [False] * tamanho_grafo
            pilha = [destino]

            while pilha:
                atual = pilha.pop()
                if not visitados[atual]:
                    visitados[atual] = True
                    for vizinho in range(tamanho_grafo):
                        if matriz_adjacencia[vizinho][atual] == 1 and not visitados[vizinho]:
                            pilha.append(vizinho)
                            fecho[vizinho][destino] = 1

        # Executa a busca em profundidade a partir de cada vértice do grafo
        for vertice in range(tamanho_grafo):
            dfs(vertice)
        return fecho
    else: 
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
