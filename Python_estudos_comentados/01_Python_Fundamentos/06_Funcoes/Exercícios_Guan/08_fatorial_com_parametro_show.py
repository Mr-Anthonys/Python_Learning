# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# fatorial() receba 2 param:
#o primeiro indique o número a calcular.
#o segundo chamado show, q será um valor lógico(opcional) indicando:
#Se será mostrado ou não a teka o  processo de calculo do fatorial


# Calcula o fatorial do valor recebido.
def fatorial (n=1, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            if c > 1:
                print(f'{c} X',end=' ')
            else:
                print(f'{c} =', end=' ')             
    return f



entrada_num = int(input("Calcular fatorial de : "))
print(fatorial(entrada_num))



