def read_graph(filename):
    with open(filename, 'r') as file:
        V = int(file.readline().strip())
        graph = [[] for _ in range(V)]
        for i in range(V):
            line = file.readline().strip().split()
            vertex = int(line[0])
            neighbors = list(map(int, line[1:]))
            graph[vertex] = neighbors
    return V, graph

def kosaraju(V, graph):
    def dfs(v, visited, stack):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)

    def transpose_graph(V, graph):
        transposed = [[] for _ in range(V)]
        for v in range(V):
            for neighbor in graph[v]:
                transposed[neighbor].append(v)
        return transposed

    def dfs_transposed(v, visited, component, transposed_graph):
        visited[v] = True
        component.append(v)
        for neighbor in transposed_graph[v]:
            if not visited[neighbor]:
                dfs_transposed(neighbor, visited, component, transposed_graph)

    stack = []
    visited = [False] * V

    # Passo 1: Preenchendo a pilha com a ordem de finalização dos vértices
    for i in range(V):
        if not visited[i]:
            dfs(i, visited, stack)

    # Passo 2: Transpor o grafo
    transposed_graph = transpose_graph(V, graph)

    # Passo 3: Processar os vértices na ordem inversa da finalização
    visited = [False] * V
    components = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs_transposed(v, visited, component, transposed_graph)
            components.append(component)
    
    return components

def main(filename):
    V, graph = read_graph(filename)
    components = kosaraju(V, graph)
    
    for i, component in enumerate(components):
        print(f"Component {i+1}: {' '.join(map(str, component))}")

# Exemplo de uso
filename = 'teste-grafos.txt'
main(filename)
