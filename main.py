# Importando a biblioteca de funções do projeto
import utils as u

# Input do usuario para receber a quantidade de vertices que o Grafo vai conter
quantidadeVertices = int(input("Insira a quantidade de vertices desejados: "))
u.limpar_tela()

# Inicialização da matriz de adjacência
matriz = [[0 for _ in range(quantidadeVertices)] for _ in range(quantidadeVertices)]

# Inicializando variaveis
opOrientacao = ""
verticeOrigem = None
sair = False

# Selecionar tipo de orientação do grafo
while opOrientacao not in ["s", "n"]:
  opOrientacao = input("O Grafo que deseja fazer eh Orientado: 's' para Sim e 'n' para Nao\nResposta: ").strip().lower()
  u.limpar_tela()

# Menu principal de interação
while not sair:
  while True:
    try:
      if opOrientacao == "n":
        print("1. Inserir arestas;")
        print("2. Excluir arestas;")
      else:
        print("1. Inserir arcos;")
        print("2. Excluir arcos;")
      print("3. Ver matriz;")
      print("4. Busca DFS;")
      print("5. Busca BFS;")
      print("6. Fecho Transitivo Direto;")
      print("7. Fecho Transitivo Inverso;")
      print("8. Verificar se o Grafico é conexo")
      print("9. Resetar Grafo;")
      print("10. Sair;")
      opcao = int(input("Opcao: "))

      if opcao < 1 or opcao > 10:
        raise ValueError
      u.limpar_tela()
      break
    except ValueError:
      print("Erro: Selecione uma opção valida!")
      input("Pressione qualquer tecla para continuar...")
      u.limpar_tela()
  
  # Inserir ligação entre os vertices
  if opcao == 1:
      u.input_origem_fim(quantidadeVertices, opOrientacao, matriz, inserir = True)

  # Remover ligação entre os vertices
  elif opcao == 2:
      u.input_origem_fim(quantidadeVertices, opOrientacao, matriz, inserir = False)

  # Mostrar Grafos
  elif opcao == 3:
    for i in range(quantidadeVertices):
      for j in range(quantidadeVertices):
        print(matriz[i][j], end=" ")
      print()
    input("Pressione qualquer tecla para continuar...")
    u.limpar_tela()

  # Metodo de Busca por Profundidade DFS
  elif opcao == 4:
    u.DFS(quantidadeVertices, matriz)

  # Metodo de Busca por Largura BFS
  elif opcao == 5:
    u.BFS(quantidadeVertices,matriz)

  # Fecho Transitivo Direto
  elif opcao == 6:
      opcao = int(input("Qual metodo de busca voce deseja usar 1.DFS; 2.BFS: "))
      if opcao == 1:
        tipoBusca = True
      else:
        tipoBusca = False
      u.limpar_tela()

      while True:
        try:
            verticeOrigem = int(input("Qual o vértice de origem: "))
            if verticeOrigem > quantidadeVertices:
                raise ValueError(f"O número máximo de vértices é de {quantidadeVertices}, por favor insira um valor válido!")
            break
        except ValueError as e:
            print("Erro: ", e)
            input("Pressione qualquer tecla para continuar...")
            u.limpar_tela()

      resultado_fecho = u.fecho_transitivo_direto(matriz, tipoBusca)
      # Exibe o resultado
      print("Fecho Transitivo Direto:")
      for linha in resultado_fecho:
          print(linha)
      input("Pressione qualquer tecla para continuar...")
      u.limpar_tela()

  # Fecho Transitivo Inverso
  elif opcao == 7:
      opcao = int(input("Qual metodo de busca voce deseja usar 1.DFS; 2.BFS: "))
      if opcao == 1:
        tipoBusca = True
      else:
        tipoBusca = False
      
      while True:
        try:
            verticeOrigem = int(input("Qual o vértice de origem: "))
            if verticeOrigem > quantidadeVertices:
                raise ValueError(f"O número máximo de vértices é de {quantidadeVertices}, por favor insira um valor válido!")
            break
        except ValueError as e:
            print("Erro: ", e)
            input("Pressione qualquer tecla para continuar...")
            u.limpar_tela()

      resultado_fecho = u.fecho_transitivo_inverso(matriz, tipoBusca)
      # Exibe o resultado
      print("Fecho Transitivo Inverso:")
      for linha in resultado_fecho:
          print(linha)
      input("Pressione qualquer tecla para continuar...")
      u.limpar_tela()

  # Verificar se o grafo é Conexo
  elif opcao == 8:
    #conexo = u.verificar_conexo(matriz)
    #print(f"Valor do conexo é: {conexo}")
    #print("O grafo é conexo." if conexo else "O grafo não é conexo.")
    u.verificar_conexo_e_identificar_sccs(matriz)
    input("Pressione qualquer tecla para continuar...")
    u.limpar_tela()

  # Resetar Grafo
  elif opcao == 9:
   quantidadeVertices = int(input("Insira a quantidade de vertices desejados: "))
   matriz = [[0 for _ in range(quantidadeVertices)] for _ in range(quantidadeVertices)]
   opOrientacao = ""
   while opOrientacao not in ["s", "n"]:
    opOrientacao = input("O Grafo que deseja fazer eh Orientado: 's' para Sim e 'n' para Nao\nResposta: ").strip().lower()
    u.limpar_tela()

  # Finalizar execução
  elif opcao == 10:
    print("Obrigado!")
    sair = True
    u.limpar_tela()