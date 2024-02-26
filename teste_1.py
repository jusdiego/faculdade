def busca_binaria_interna(elemento_inter, lista_inter, inicio_inter, fim_inter):
    if inicio_inter > fim_inter: return False
    meio = (inicio_inter+fim_inter)//2
    if elemento_inter == lista_inter[meio]: print(meio)
    if elemento_inter < lista_inter[meio]: 
        return busca_binaria_interna(elemento_inter, lista_inter, inicio_inter, meio-1)
    return busca_binaria_interna(elemento_inter, lista_inter, meio+1, fim_inter)

elementos_teste_2 = [4, 17, 48, 92, 123]

def busca_binaria_r(x, L, inicio, fim):
    if inicio > fim: return False
    meio = (inicio+fim)//2
    if x == L[meio]: print(meio)
    if x <   L[meio]: return busca_binaria_r(x, L, inicio, meio-1)
    return busca_binaria_r(x, L, meio+1, fim)
    print('Oi')

def bbr(x, L): # wrapper
    return busca_binaria_interna(x, L, 0, len(L)-1)

# bbr(123, elementos_teste_2)


def busca_binaria1(x, L):
    inicio = 0
    fim = len(L)-1
    while inicio <= fim:
        meio = (inicio+fim)//2
        if x == L[meio]:       return True
        elif x < L[meio]:  fim = meio - 1
        else:                  inicio = meio + 1
    return False


