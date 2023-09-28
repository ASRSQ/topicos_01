from data_structure.constroiGrafo import constroi_grafo_de_arquivo
from data_structure.arvore_AVL import AVLTree

def prim_avl(graph):
    # Inicialize a árvore AVL vazia
    tree = AVLTree()
    
    # Escolha um vértice arbitrário como vértice inicial
    start_vertex = list(graph.keys())[0]
    
    # Insira o vértice inicial na árvore com peso zero
    tree.insert(start_vertex, 0)
    
    mst = []  # Lista para armazenar as arestas da árvore geradora mínima
    total_weight = 0  # Variável para armazenar o peso total da AGM
    
    while len(tree) < len(graph):
        min_weight = float('inf')
        min_vertex = None
        
        # Para cada vértice que não está na árvore AVL
        for vertex, edges in graph.items():
            if not tree.contains(vertex):
                # Calcule o peso da menor aresta que o conecta à árvore corrente
                for edge_vertex, weight in edges:
                    if tree.contains(edge_vertex) and weight < min_weight:
                        min_weight = weight
                        min_vertex = vertex
        
        if min_vertex:
            # Remova o vértice com a menor chave (menor peso) da árvore AVL
            tree.delete(min_vertex)
            
            # Adicione o vértice selecionado à árvore corrente
            mst.append((min_vertex, min_weight))
            tree.insert(min_vertex, min_weight)
            
            # Adicione o peso da aresta à variável total_weight
            total_weight += min_weight
    
    return mst, total_weight
# Lê o arquivo desejado e constroi o grafo com os dados
filename = './instances/dados.txt'
graph = constroi_grafo_de_arquivo(filename)

#Inicializa o algoritmo de prim_avl e imprime as arestas e pesos correspondentes a cada aresta e por fim o peso total
minimum_spanning_tree, total_weight = prim_avl(graph)
print("Arestas da árvore geradora mínima:")
for edge, weight in minimum_spanning_tree:
    print(f"Aresta {edge} com peso {weight}")
print(f"Peso total da árvore geradora mínima: {total_weight}")