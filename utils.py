import os
from collections import deque

# limpar console
def limpar_tela():
  os.system('cls')  # Windows

# Função criada para dar input no vertice de origem e de fim para finalidade de inserir aresta ou arco, ou remove-los 
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

    # Se for True significa que é para inserir
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
    # Se for False significa que é para remover
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

# Função feita para efetuar a busca por Profundidade
def DFS(quantidadeVertices, matriz, vertice=1):
    # Inicializando variaveis
    pilha = []
    visitas = [0] * quantidadeVertices  # Inicializando a lista de visitas com zeros
    fecho = [[0] * quantidadeVertices for _ in range(quantidadeVertices)]
    vertices_visitados = []  # Lista para armazenar os vértices visitados em ordem

    while True:
        try:
            vertice = int(input("Qual o vértice de origem: "))
            if vertice > quantidadeVertices:
                raise ValueError(f"O número máximo de vértices é de {quantidadeVertices}, por favor insira um valor válido!")
            break
        except ValueError as e:
            print("Erro: ", e)
            input("Pressione qualquer tecla para continuar...")
            limpar_tela()

    pilha.append(vertice)  # Adiciona o vértice de origem à pilha
    while pilha:
        atual = pilha.pop()
        if not visitas[atual]:
            visitas[atual] = True
            vertices_visitados.append(atual+1)  # Adiciona o vértice atual à lista de visitados
            for i in range(quantidadeVertices):
                if matriz[i][atual] == 1 and not visitas[i]:
                    pilha.append(i)
                    fecho[i][vertice] = 1

    ultimo_elemento = vertices_visitados.pop()  # Remove e captura o último elemento
    vertices_visitados.insert(0, ultimo_elemento)
    print("Vértices visitados em ordem:", vertices_visitados)  # Imprime os vértices visitados em ordem

def BFS(quantidadeVertices, matriz, vertice=1):

    fila = deque()  # Inicializa uma fila vazia
    visitas = [0] * quantidadeVertices  # Inicializa a lista de visitas com zeros
    vertices_visitados = []  # Lista para armazenar os vértices visitados em ordem

    while True:
        try:
            vertice = int(input("Qual o vértice de origem: "))
            if vertice > quantidadeVertices:
                raise ValueError(f"O número máximo de vértices é de {quantidadeVertices}, por favor insira um valor válido!")
            break
        except ValueError as e:
            print("Erro: ", e)
            input("Pressione qualquer tecla para continuar...")
            limpar_tela()

    fila.append(vertice)  # Adiciona o vértice de origem à fila
    visitas[vertice - 1] = 1  # Marca o vértice de origem como visitado
    vertices_visitados.append(vertice)  # Adiciona o vértice de origem à lista de visitados

    while fila:
        verticeAtual = fila.popleft()  # Remove o primeiro elemento da fila
        for i in range(quantidadeVertices):
            if matriz[verticeAtual - 1][i] and not visitas[i]:
                fila.append(i + 1)  # Adiciona o vértice adjacente à fila
                visitas[i] = 1  # Marca o vértice adjacente como visitado
                vertices_visitados.append(i + 1)  # Adiciona o vértice adjacente à lista de visitados

    print("Vértices visitados em ordem:", vertices_visitados)  # Imprime os vértices visitados em ordem

def fecho_transitivo_direto(matriz, tipoBusca):
    tamanho_grafo = len(matriz)
    fecho = [[0] * tamanho_grafo for _ in range(tamanho_grafo)]

    if tipoBusca == True:
        def dfs(destino):
            visitados = [False] * tamanho_grafo
            pilha = [destino]

            while pilha:
                atual = pilha.pop()
                if not visitados[atual]:
                    visitados[atual] = True
                    for i in range(tamanho_grafo):
                        if matriz[i][atual] == 1 and not visitados[i]:
                            pilha.append(i)
                            fecho[i][destino] = 1

        # Executa a busca em profundidade a partir de cada vértice do grafo
        for vertice in range(tamanho_grafo):
            dfs(vertice)
        for i in range(tamanho_grafo):
            fecho[i][i] = 1
        return fecho
    else: 
        def bfs(destino):
            visitados = [False] * tamanho_grafo
            fila = deque([destino])

            while fila:
                atual = fila.popleft()
                for i in range(tamanho_grafo):
                    if matriz[i][atual] == 1 and not visitados[i]:
                        visitados[i] = True
                        fila.append(i)
                        fecho[i][destino] = 1

        # Executa a busca em largura a partir de cada vértice do grafo
        for vertice in range(tamanho_grafo):
            bfs(vertice)
        return fecho

def fecho_transitivo_inverso(matriz, tipoBusca):
    tamanho_grafo = len(matriz)
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
                    for i in range(tamanho_grafo):
                        if matriz[i][atual] == 1 and not visitados[i]:
                            pilha.append(i)
                            fecho[i][destino] = 1

        # Executa a busca em profundidade a partir de cada vértice do grafo
        for vertice in range(tamanho_grafo):
            dfs(vertice)
        for i in range(tamanho_grafo):
            fecho[i][i] = 1
        return fecho
    else: 
        def bfs(destino):
            visitados = [False] * tamanho_grafo
            fila = deque([destino])

            while fila:
                atual = fila.popleft()
                for i in range(tamanho_grafo):
                    if matriz[i][atual] == 1 and not visitados[i]:
                        visitados[i] = True
                        fila.append(i)
                        fecho[i][destino] = 1

        # Executa a busca em largura a partir de cada vértice do grafo
        for vertice in range(tamanho_grafo):
            bfs(vertice)
        return fecho

# Verificar se o grafo é conexo
def verificar_conexo(matriz):
    tamanho_grafo = len(matriz)
    # Calcula o fecho transitivo direto e o fecho transitivo inverso do grafo
    fecho_direto = fecho_transitivo_direto(matriz, tipoBusca=True)
    fecho_inverso = fecho_transitivo_inverso(matriz, tipoBusca=False)

    # Verifica se todos os vértices são alcançáveis em ambos os fechos
    for i in range(tamanho_grafo):
        for j in range(tamanho_grafo):
            if not (fecho_direto[i][j] and fecho_inverso[i][j]):
                return False  # Se um vértice não for alcançável, o grafo não é conexo
    return True  # Se todos os vértices forem alcançáveis, o grafo é conexo

def tarjan_scc(grafo):
    # Calcula o número de vértices no grafo
    n = len(grafo)
    
    # Lista para marcar se um vértice foi visitado durante a busca
    visitado = [False] * n
    
    # Lista para armazenar a ordem de descoberta de cada vértice durante a busca
    ordem_descoberta = [-1] * n
    
    # Lista para armazenar o valor da baixa ligação de cada vértice durante a busca
    baixa_ligacao = [-1] * n
    
    # Pilha para manter os vértices visitados durante a busca
    pilha = []
    
    # Lista para armazenar os componentes fortemente conectados encontrados
    sccs = []

    # Função de busca em profundidade recursiva
    def dfs(v, tempo):
        # Atribui a ordem de descoberta e baixa ligação para o vértice atual
        ordem_descoberta[v] = tempo
        baixa_ligacao[v] = tempo
        tempo += 1
        
        # Adiciona o vértice à pilha e marca como visitado
        pilha.append(v)
        visitado[v] = True

        # Explora todos os vizinhos do vértice atual
        for u in grafo[v]:
            # Se o vizinho não foi visitado ainda
            if ordem_descoberta[u] == -1:
                # Chama recursivamente a DFS para o vizinho
                tempo = dfs(u, tempo)
                # Atualiza a baixa ligação do vértice atual
                baixa_ligacao[v] = min(baixa_ligacao[v], baixa_ligacao[u])
            # Se o vizinho já foi visitado e está na pilha (forma um ciclo)
            elif visitado[u]:
                # Atualiza a baixa ligação do vértice atual
                baixa_ligacao[v] = min(baixa_ligacao[v], ordem_descoberta[u])

        # Verifica se o vértice é a raiz de um componente fortemente conectado
        if baixa_ligacao[v] == ordem_descoberta[v]:
            # Inicializa um novo componente fortemente conectado
            scc = []
            while True:
                # Remove vértices da pilha até alcançar o vértice atual
                u = pilha.pop()
                visitado[u] = False
                scc.append(u+1)
                if u == v:
                    break
            # Adiciona o componente fortemente conectado à lista
            sccs.append(scc)

        return tempo

    # Inicia a busca em profundidade para todos os vértices não visitados
    for v in range(n):
        if ordem_descoberta[v] == -1:
            dfs(v, 0)

    return sccs
def verificar_conexo_e_identificar_sccs(matriz):
    tamanho_grafo = len(matriz)
    fecho_direto = fecho_transitivo_direto(matriz, tipoBusca=True)
    fecho_inverso = fecho_transitivo_inverso(matriz, tipoBusca=True)

    # Verificar se todos os vértices são alcançáveis em ambos os fechos
    for i in range(tamanho_grafo):
        for j in range(tamanho_grafo):
            if not (fecho_direto[i][j] and fecho_inverso[i][j]):
                print("O grafo não é conexo.")
                sccs = tarjan_scc(matriz)
                print("Subgrafos fortemente conexos:")
                for scc in sccs:
                    print(scc)
                return
    
    print("O grafo é conexo.")