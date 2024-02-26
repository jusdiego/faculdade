def busca_sequencial6(x, L):
    for i, valor in enumerate(L):
        if x == valor:
            return print(i)
    return None

def busca_sequencial7(x, L, n): # n = tamanho lógico de L
    if n == 0: return None
    if x == L[n-1]: return print(n-1)
    return busca_sequencial7(x, L, n-1)

elementos_teste_1 = [1, 5, 33, 144, -2048]
elementos_teste_1 = []
elementos_teste_2 = [1,2,3,4,5,6,7,8,9,10]


busca_sequencial6(33, elementos_teste_1)
busca_sequencial7(33, elementos_teste_1, len(elementos_teste_1))