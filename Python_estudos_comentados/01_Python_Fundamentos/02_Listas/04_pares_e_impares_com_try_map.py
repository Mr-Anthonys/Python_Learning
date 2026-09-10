# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio 2. (Usando TRY e MAP{})

#Leia n valores númericos e cadastre em uma unica lista que mantenha os valores separados entre PARES e IMPARES.
#No final mostre os valores en ordem crescente 

lista_num_final = [[],[]]#Lista com 2 listras encadeadas

for c in range(0,7):#Laço até 7
    while True:#Verificação
        try:#Tente
            entrada_num = (int(input(f'Digite o {c+1}º Valor: ')))#entrada do valor    
            if entrada_num % 2 == 0:#se a entrada for PAR
                print(f'Valor {entrada_num} Adicionado com sucesso na lista de PAR.')
                lista_num_final[0].append(entrada_num)#lista aprende par na posição 0
            else:#se a entrada for impar
                print(f'Valor {entrada_num} adicionado com sucesso na lista ÍMPAR.')
                lista_num_final[1].append(entrada_num)
            break# se tudo deu certo saia do while voltando para outra volta do laço FOR                
        except ValueError, TypeError:# Verificação de erro
            print(f'Entrada inválida ! Informe apenas NÚMEROS.')#Aviso do erro e volta para o WHILE, e não para o FOR

#Resultado
        
print(f'Valores informados em uma única lista ----> {lista_num_final}')
print(f'Valores PARES ----> {lista_num_final[0]}')
print(f'Valores ÍMPARES ----> {lista_num_final[1]}')
#Ordenando valores para o print usando o .join()

#Transformando em TEXTO para usar o .join

pares_texto = map(str, sorted(lista_num_final[0]))

print(f'Valores PARES EM ORDEM ----> {"| ".join(pares_texto)}')


#join colocando "-" entre os valores, depois o MAP mudando pra STR e colocando em ordem com SORTED
print(f'Valores ÍMPARES EM ORDEM ----> {"| ".join(map(str , sorted(lista_num_final[1])))}')# 

