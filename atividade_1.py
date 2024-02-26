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

# print(f"A lista de teste possui {N} elementos no total")

def busca_lin_1(lista, elemento):
    """A função retorna o índice do elemento na lista,
    caso o elemento não esteja na lista, retorna None"""
    for i in range(len(lista)):
        if lista[i] == elemento:
            print(i)
            return True
    return None 

def busca_lin_rec_1(lista, elemento):
    """Versão recursiva da busca linear"""
    def busca_linear(lista, elemento, tamanho):
        if tamanho == 0: return None 
        if elemento == lista[tamanho-1]: return print(tamanho-1) 
        return busca_linear(lista, elemento, tamanho-1)
    
    buscar = busca_linear(lista, elemento, len(lista)-1)
    return buscar

def busca_lin_M(lista, elemento):
    """A função retorna o índice do elemento na lista,
    caso o elemento não esteja na lista, retorna None"""
    lista_indices = []
    for i in range(len(lista)):
        if lista[i] == elemento:
            lista_indices.append(i)
    return print(lista_indices) 

def busca_lin_rec_M(lista, elemento):
    """Versão recursiva da busca linear"""
    lista_indices = []
    def busca_linear(lista, elemento, tamanho):
        if tamanho == 0: return None 
        if elemento == lista[tamanho-1]: lista_indices.append(tamanho-1) 
        return busca_linear(lista, elemento, tamanho-1)
    
    busca_linear(lista, elemento, len(lista)-1)
    return print(lista_indices)

def verificar_repetidos(lista):
    """Retorna True se há elementos repetidos na lista e
    False caso contrário"""
    elementos_unicos = set()
    for i in lista:
        if i in elementos_unicos:
            print('A valores iguais na lista')
            return True
        else:
            elementos_unicos.add(i) 
    print('Não há valores iguais na lista') 
    return False

def verificar_ordenacao(lista):
    for i in range(len(lista)-1):
       if lista[i] > lista[i+1]:
          print('Lista não ordenada')
          return False 
    print('Lista Ordenada') 
    return True

def busca_bin_1(lista, elemento):
    """A função retorna o índice do elemento na lista,
    caso o elemento não esteja na lista, retorna None"""
    if not verificar_ordenacao(lista): return
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio+fim)//2
        if elemento == lista[meio]:  return print(meio)
        elif elemento < lista[meio]: fim = meio - 1
        else:                        inicio = meio + 1
    return print('Elemento não encontrado')


def busca_bin_rec_1(lista, elemento):
    """Versão recursiva da busca binária""" 
    if not verificar_ordenacao(lista): return
    inicio = 0
    fim = len(lista)-1
    return busca_binaria(elemento, lista, inicio, fim) 

def busca_binaria(elemento_inter, lista_inter, inicio_inter, fim_inter):
    if inicio_inter > fim_inter: return 
    meio = (inicio_inter+fim_inter)//2
    if elemento_inter == lista_inter[meio]: print(meio)
    if elemento_inter < lista_inter[meio]: 
        return busca_binaria(elemento_inter, lista_inter, inicio_inter, meio-1)
    return busca_binaria(elemento_inter, lista_inter, meio+1, fim_inter)
    

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

elementos_teste_1 = [1, 5, 33, 144, -2048]
elementos_teste_2 = [1,2,3,4,5,6,7,8,9,10]
lista1 = [x for x in range(1,50)]

arvore = construir_arvore(lista_teste2)
p(arvore)
print(lista_teste2)


1,2,1,3,4,5,6