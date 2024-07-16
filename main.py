def ler_grafo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        V = int(arquivo.readline().strip())
        grafo = [[] for _ in range(V)]
        for i in range(V):
            linha = arquivo.readline().strip().split()
            vertice = int(linha[0])
            vizinhos = list(map(int, linha[1:]))
            grafo[vertice] = vizinhos
    return V, grafo

def kosaraju(V, grafo):
    def dfs(v, visitado, pilha):
        visitado[v] = True
        for vizinho in grafo[v]:
            if not visitado[vizinho]:
                dfs(vizinho, visitado, pilha)
        pilha.append(v)

    def transpor_grafo(V, grafo):
        transposto = [[] for _ in range(V)]
        for v in range(V):
            for vizinho in grafo[v]:
                transposto[vizinho].append(v)
        return transposto

    def dfs_transposto(v, visitado, componente, grafo_transposto):
        visitado[v] = True
        componente.append(v)
        for vizinho in grafo_transposto[v]:
            if not visitado[vizinho]:
                dfs_transposto(vizinho, visitado, componente, grafo_transposto)

    pilha = []
    visitado = [False] * V

    # Passo 1: Preenchendo a pilha com a ordem de finalização dos vértices
    for i in range(V):
        if not visitado[i]:
            dfs(i, visitado, pilha)

    # Passo 2: Transpor o grafo
    grafo_transposto = transpor_grafo(V, grafo)

    # Passo 3: Processar os vértices na ordem inversa da finalização
    visitado = [False] * V
    componentes = []
    while pilha:
        v = pilha.pop()
        if not visitado[v]:
            componente = []
            dfs_transposto(v, visitado, componente, grafo_transposto)
            componentes.append(componente)
    
    return componentes

def main(nome_arquivo):
    V, grafo = ler_grafo(nome_arquivo)
    componentes = kosaraju(V, grafo)
    
    for i, componente in enumerate(componentes):
        print(f"Componente {i+1}: {' '.join(map(str, componente))}")

# Exemplo de uso
nome_arquivo = 'teste-grafos.txt'
main(nome_arquivo)
