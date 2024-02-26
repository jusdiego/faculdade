
import pprint   
import numpy as np

# NÃO MODIFICAR O CÓDIGO DESTA CÉLULA
np.random.seed(0)

N = 511
L = 1000000
lista_teste1 = list([np.random.randint(-L, L) for _ in range(N)])
lista_teste2 = sorted(list([np.random.randint(-L, L) for _ in range(N)]))


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


def construir_arvore(lista):
    """
    Constrói a árvore de busca binária com os dados de lista e
    retorna o dicionário com os campos:
    
    arvore = {
        'valor': xxx,
        'indice': idx,
        'esquerda': {galho_esquerda},
        'direita': {galho_direita}
    }
    
    Se o nó for uma folha, então:
        'esquerda': None,
        'direita': None
    """
    def build_arvore(lista, inicio, fim):
        if inicio > fim:
            return None
        
        if inicio == fim:
            return {
                'valor': lista[inicio],
                'indice': inicio,
                'esquerda': None,
                'direta': None
            }
        
        meio = (inicio + fim) // 2
        nodo = {
            'valor': lista[meio],
            'indice': meio,
            'esquerda': build_arvore(lista, inicio, meio - 1),
            'direita': build_arvore(lista, meio + 1, fim)
        }
        return nodo
    
    arvore = build_arvore(lista, 0, len(lista) - 1)

    return arvore

def busca_arvore_rec(arvore, elemento):
    if arvore['valor'] == elemento:
       return print(arvore['indice'])
    elif arvore['valor'] > elemento:
        if 'esquerda' in arvore.keys():
            return busca_arvore_rec(arvore['esquerda'], elemento)
        else:
           return False
    elif arvore['valor'] < elemento:
        if 'direita' in arvore.keys():
            return busca_arvore_rec(arvore['direita'], elemento)
    else:
        return False



lista = [1,2,3,4,5,6,7,8,9,10]
arvore = construir_arvore(lista)
busca_arvore_rec(arvore, 5)
