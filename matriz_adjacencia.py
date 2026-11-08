def criar_grafo():
    return {"vertices": [], "matriz": []}


def inserir_vertice(g, v):
    if v not in g["vertices"]:
        g["vertices"].append(v)
        for linha in g["matriz"]:
            linha.append(0)
        nova_linha = [0] * len(g["vertices"])
        g["matriz"].append(nova_linha)


def inserir_aresta(g, u, v):
    inserir_vertice(g, u)
    inserir_vertice(g, v)
    i = g["vertices"].index(u)
    j = g["vertices"].index(v)
    g["matriz"][i][j] = 1
    g["matriz"][j][i] = 1


def remover_vertice(g, v):
    if v in g["vertices"]:
        idx = g["vertices"].index(v)
        g["vertices"].pop(idx)
        g["matriz"].pop(idx)
        for linha in g["matriz"]:
            linha.pop(idx)


def remover_aresta(g, u, v):
    if u in g["vertices"] and v in g["vertices"]:
        i = g["vertices"].index(u)
        j = g["vertices"].index(v)
        g["matriz"][i][j] = 0
        g["matriz"][j][i] = 0


def grau_vertice(g, v):
    if v not in g["vertices"]:
        return 0
    idx = g["vertices"].index(v)
    return sum(g["matriz"][idx])


def existe_aresta(g, u, v):
    if u in g["vertices"] and v in g["vertices"]:
        i = g["vertices"].index(u)
        j = g["vertices"].index(v)
        return g["matriz"][i][j] == 1
    return False


def listar_vizinhos(g, v):
    if v not in g["vertices"]:
        return []
    idx = g["vertices"].index(v)
    vizinhos = []
    for j, val in enumerate(g["matriz"][idx]):
        if val == 1:
            vizinhos.append(g["vertices"][j])
    return vizinhos


def percurso_valido(g, caminho):
    for i in range(len(caminho) - 1):
        if not existe_aresta(g, caminho[i], caminho[i+1]):
            return False
    return True


def main():
    grafo = criar_grafo()
    
    # Inserindo
    inserir_aresta(grafo, "A", "B")
    inserir_aresta(grafo, "B", "C")
    inserir_aresta(grafo, "C", "A")
    
    print("MATRIZ DE ADJACÊNCIA")
    print("Vértices:", grafo["vertices"])
    print("Matriz inicial:")
    for linha in grafo["matriz"]:
        print(linha)
        
    print("Existe aresta entre A e B?", existe_aresta(grafo, "A", "B"))
    print("Vizinhos de B:", listar_vizinhos(grafo, "B"))
    print("Grau do vértice B:", grau_vertice(grafo, "B"))
    print("Percurso válido ['A', 'B', 'C']?", percurso_valido(grafo, ["A", "B", "C"]))
    
    remover_aresta(grafo, "A", "B")
    print("\nMatriz após remover aresta (A, B):")
    for linha in grafo["matriz"]:
        print(linha)
    
    remover_vertice(grafo, "C")
    print("\nVértices após remover 'C':", grafo["vertices"])
    print("Matriz após remover 'C':")
    for linha in grafo["matriz"]:
        print(linha)


if __name__ == "__main__":
    main()