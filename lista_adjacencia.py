def criar_grafo():
    return {"adj": {}}


def inserir_vertice(g, v):
    if v not in g["adj"]:
        g["adj"][v] = []


def inserir_aresta(g, u, v):
    inserir_vertice(g, u)
    inserir_vertice(g, v)
    if v not in g["adj"][u]:
        g["adj"][u].append(v)
    if u not in g["adj"][v]:
        g["adj"][v].append(u)


def remover_vertice(g, v):
    if v in g["adj"]:
        del g["adj"][v]
    for vertice in g["adj"]:
        if v in g["adj"][vertice]:
            g["adj"][vertice].remove(v)


def remover_aresta(g, u, v):
    if u in g["adj"] and v in g["adj"][u]:
        g["adj"][u].remove(v)
    if v in g["adj"] and u in g["adj"][v]:
        g["adj"][v].remove(u)


def grau_vertice(g, v):
    return len(g["adj"].get(v, []))


def existe_aresta(g, u, v):
    return u in g["adj"] and v in g["adj"][u]


def listar_vizinhos(g, v):
    return g["adj"].get(v, [])


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
    
    print("LISTA DE ADJACÊNCIA")
    print("Estrutura:", grafo["adj"])
    print("Existe aresta entre A e B?", existe_aresta(grafo, "A", "B"))
    print("Vizinhos de B:", listar_vizinhos(grafo, "B"))
    print("Grau do vértice B:", grau_vertice(grafo, "B"))
    print("Percurso válido ['A', 'B', 'C']?", percurso_valido(grafo, ["A", "B", "C"]))
  
    remover_aresta(grafo, "A", "B")
    print("\nApós remover aresta (A, B):", grafo["adj"])
    
    remover_vertice(grafo, "C")
    print("Após remover vértice 'C':", grafo["adj"])


if __name__ == "__main__":
    main()