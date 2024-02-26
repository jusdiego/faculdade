import numpy as np
import pprint   

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# NÃO MODIFICAR O CÓDIGO DESTA CÉLULA
np.random.seed(0)

N = 511
L = 1000000
lista_teste1 = list([np.random.randint(-L, L) for _ in range(N)])
lista_teste2 = sorted(list([np.random.randint(-L, L) for _ in range(N)]))

def verificar_ordenacao(lista):
    for i in range(len(lista)-1):
       if lista[i] > lista[i+1]:
          print('Lista não ordenada')
          return False 
    print('Lista Ordenada') 
    return True

def busca_bin_arvore_1(arvore, elemento):
    """Busca binária usando a árvore de busca"""
    while arvore is not None:
        if elemento == arvore['valor']:
            return print(arvore['indice'])
        elif elemento < arvore['valor']:
            arvore = arvore['esquerda']
        else:
            arvore = arvore['direita']
    return print('Elemento não encontrado')

def busca_bin_arvore_rec_1(arvore, elemento):
    """Versão recursiva da busca binária usando a árvore de busca"""
    if arvore is None:
            return print('Elemento não encontrado')
        
    if elemento == arvore['valor']:
        return print(arvore['indice'])
    elif elemento < arvore['valor']:
        return busca_bin_arvore_rec_1(arvore['esquerda'], elemento)
    else:
        return busca_bin_arvore_rec_1(arvore['direita'], elemento)
    
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
                'direita': None
            }
        
        meio = (inicio + fim) // 2
        arvore_binaria = {
            'valor': lista[meio],
            'indice': meio,
            'esquerda': build_arvore(lista, inicio, meio - 1),
            'direita': build_arvore(lista, meio + 1, fim)
        }
        return arvore_binaria
    
    if not verificar_ordenacao(lista): 
        return print('Não é possivel criar uma arvore desse lista')
    
    arvore = build_arvore(lista, 0, len(lista) - 1)

    return arvore

elementos_teste = [-2048, 1, 5, 33, 144]

arvore = construir_arvore(elementos_teste)
p(arvore)
print(elementos_teste)
