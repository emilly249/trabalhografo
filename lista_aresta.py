def criar_grafo():
    return {"vertices": [], "arestas": []}


def inserir_vertice(g, v):
    if v not in g["vertices"]:
        g["vertices"].append(v)


def inserir_aresta(g, u, v):
    inserir_vertice(g, u)
    inserir_vertice(g, v)
    if (u, v) not in g["arestas"] and (v, u) not in g["arestas"]:
        g["arestas"].append((u, v))


def remover_vertice(g, v):
    if v in g["vertices"]:
        g["vertices"].remove(v)
    g["arestas"] = [a for a in g["arestas"] if a[0] != v and a[1] != v]


def remover_aresta(g, u, v):
    g["arestas"] = [a for a in g["arestas"] if not ((a[0] == u and a[1] == v) or (a[0] == v and a[1] == u))]


def grau_vertice(g, v):
    contador = 0
    for a in g["arestas"]:
        if a[0] == v or a[1] == v:
            contador += 1
    return contador


def existe_aresta(g, u, v):
    return (u, v) in g["arestas"] or (v, u) in g["arestas"]


def listar_vizinhos(g, v):
    vizinhos = []
    for a in g["arestas"]:
        if a[0] == v:
            vizinhos.append(a[1])
        elif a[1] == v:
            vizinhos.append(a[0])
    return vizinhos


def percurso_valido(g, caminho):
    for i in range(len(caminho) - 1):
        if not existe_aresta(g, caminho[i], caminho[i+1]):
            return False
    return True


def main():
    grafo = criar_grafo()
    
    inserir_aresta(grafo, "A", "B")
    inserir_aresta(grafo, "B", "C")
    inserir_aresta(grafo, "C", "A")
    
    print("LISTA DE ARESTAS")
    print("Vértices:", grafo["vertices"])
    print("Arestas:", grafo["arestas"])
    print("Existe aresta entre A e B?", existe_aresta(grafo, "A", "B"))
    print("Vizinhos de B:", listar_vizinhos(grafo, "B"))
    print("Grau do vértice B:", grau_vertice(grafo, "B"))
    print("Percurso válido ['A', 'B', 'C']?", percurso_valido(grafo, ["A", "B", "C"]))
   
    remover_aresta(grafo, "A", "B")
    print("\nArestas após remover (A, B):", grafo["arestas"])
    
    remover_vertice(grafo, "C")
    print("Vértices após remover 'C':", grafo["vertices"])
    print("Arestas após remover 'C':", grafo["arestas"])


if __name__ == "__main__":
    main()