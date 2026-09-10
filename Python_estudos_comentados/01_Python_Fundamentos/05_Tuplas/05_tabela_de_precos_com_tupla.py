# ============================================================
# Exercício de tuplas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#TABELA

tabela = ('Picanha', 66.90, 'Contra-Filé', 45.00, 'Acém', 35.00, 'Alcatra', 38.00, 'Costela', 38.00, 'Linguiça', 21.00, 
          'bisteca', 28.00 )
print('='*45)
print(f'{"TABELA DE PREÇOS":^40}')
print('='*45)

#Para cada posição ma faixa de 0 até numero total da tupla "len(tabela)"
for posiçao in range(0, len(tabela)):


    #Condição para verificar os 1 iten se é PAR)
    #No caso da Tupla acima os nomes das carnes são 0 = picanha, 2 = contra file.... então são os pares da tupla
    if posiçao % 2 == 0:
        
        print(f'{tabela[posiçao]:.<33}', end='')#imprimindo o item da tabela na posição (:.<30) pontos alinhados a <esq
    else:
        print(f' R$:{tabela[posiçao]:>6.2f}')
print('='*45)
