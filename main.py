# Importando a biblioteca de funções do projeto
import utils as u

#TODO Fazer testes com orientação. Testar para ver se o fecho transitivo direto e inverso estão funcionando corretamente! E por fim ver o notas!!


# Input do usuario para receber a quantidade de vertices que o Grafo vai conter
quantidadeVertices = int(input("Insira a quantidade de vertices desejados: "))
u.limpar_tela()

# Inicialização da matriz de adjacência
matriz = [[0 for _ in range(quantidadeVertices)] for _ in range(quantidadeVertices)]

opOrientacao = ""
verticeOrigem = None

while opOrientacao not in ["s", "n"]:
  opOrientacao = input("O Grafo que deseja fazer eh Orientado: 's' para Sim e 'n' para Nao\nResposta: ").strip().lower()
  u.limpar_tela()

sair = False

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
      print("6. Resetar Grafo;")
      print("7. Fecho Transitivo Direto;")
      print("8. Fecho Transitivo Inverso;")
      print("9. Sair;")
      opcao = int(input("Opcao: "))
      if opcao < 1 or opcao > 9:
        raise ValueError
      u.limpar_tela()
      break
    except ValueError:
      print("Erro: Selecione uma opção valida!")
      input("Pressione qualquer tecla para continuar...")
      u.limpar_tela()

  if opcao not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("Opção inválida. Por favor, escolha uma opção válida.")
    u.limpar_tela()
    continue

  if opcao == 1:
      u.input_origem_fim(quantidadeVertices, opOrientacao, matriz, inserir = True)

  elif opcao == 2:
      u.input_origem_fim(quantidadeVertices, opOrientacao, matriz, inserir = False)

  elif opcao == 3:
    for i in range(quantidadeVertices):
      for j in range(quantidadeVertices):
        print(matriz[i][j], end=" ")
      print()
    input("Pressione qualquer tecla para continuar...")
    u.limpar_tela()

  elif opcao == 4:
    u.DFS(quantidadeVertices, matriz)

  elif opcao == 5:
    u.BFS(quantidadeVertices,matriz)

  elif opcao == 6:
   quantidadeVertices = int(input("Insira a quantidade de vertices desejados: "))
   matriz = [[0 for _ in range(quantidadeVertices)] for _ in range(quantidadeVertices)]
   opOrientacao = ""
   while opOrientacao not in ["s", "n"]:
    opOrientacao = input("O Grafo que deseja fazer eh Orientado: 's' para Sim e 'n' para Nao\nResposta: ").strip().lower()
    u.limpar_tela()

  elif opcao == 7:
      opcao = int(input("Qual metodo de busca voce deseja usar 1.DFS; 2.BFS: "))
      if opcao == 1:
        tipoBusca = True
      else:
        tipoBusca = False

      resultado_fecho = u.fecho_transitivo_direto(matriz, tipoBusca)
      # Exibe o resultado
      print("Fecho Transitivo Direto:")
      for linha in resultado_fecho:
          print(linha)
      input("Pressione qualquer tecla para continuar...")
      u.limpar_tela()

  elif opcao == 8:
      opcao = int(input("Qual metodo de busca voce deseja usar 1.DFS; 2.BFS: "))
      if opcao == 1:
        tipoBusca = True
      else:
        tipoBusca = False
        
      resultado_fecho = u.fecho_transitivo_inverso(matriz, tipoBusca)
      # Exibe o resultado
      print("Fecho Transitivo Inverso:")
      for linha in resultado_fecho:
          print(linha)
      input("Pressione qualquer tecla para continuar...")
      u.limpar_tela()

  elif opcao == 9:
    print("Obrigado!")
    sair = True
    u.limpar_tela()

