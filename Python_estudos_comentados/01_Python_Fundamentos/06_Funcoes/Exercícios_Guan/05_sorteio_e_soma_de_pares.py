# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#- Faça um programa q tenha uma lista chamada e 2 funções:
#- sorteia() e soma_par().
#- A primeira função vai sortear 5 números e colocá-los dentro de uma lista.
#- A segunda função vai mostrar a soma entre todos os valores PARES sorteados.

from random import randint


# Gera/seleciona valores aleatórios conforme a proposta do exercício.
def sorteia():
    """ Sorteia 5 números aleatórios de 1 a 100 e exibe na tela."""
    num_sorteados = []
    for n in range(1, 6):
        num_sorteados.append(randint(1, 100))

    print(f'valores sorteados ---> {num_sorteados}')
    return num_sorteados

# Soma os valores pares recebidos.
def soma_par(lista): 
    """Filtra e soma os números pares de uma lista de inteiros.

    Args:
        lista (list): Uma lista contendo os números inteiros a serem analisados.

    Returns:
        list: Uma nova lista contendo apenas os valores pares encontrados.
    """   
    par_lista = []
    for n in lista:
        if n % 2 == 0:
            par_lista.append(n)
        else:
            continue
        if len(par_lista) == 0:
            print(f'Nenhum valor PAR informado.')
    print(f'Lista com números PAR --> {par_lista}')
    print(f'Soma dos valores PARES: {sum(par_lista)}')
    return par_lista


numeros = sorteia()
pares = soma_par(numeros)

