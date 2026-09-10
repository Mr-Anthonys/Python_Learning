# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#-Exercicio 3
#-Faça um programa que tenha um função chamada CONTADOR().
#-Que Receba três parâmetros: início, fim e passo.
#-Realize 3 contagens:
#-A) de 1 até 10, de 1 em 1
#-B) de 10 até 0, de 2 em 2
#-C) Uma contagem persanolizada.


# Tentativa com for.
# def contador(i, f, p):
#     print(f'-='*30)
#     print(f'Contador de {i} até {f} de {p} e {p}.'.replace('-' , ''))
#     for c in range(i, f+1, p):
#         print(f' |{c}|', end=' ')
#     print()

     
     
# #-Programa principal
# #-A) de 1 até 10, de 1 em 1
# contador(1, 10, 1)

# #-B) de 10 até 0, de 2 em 2
# contador(10, 0, -2)


# #-C) Uma contagem persanolizada.
# print(f'Sua vez de personalizar uma contagem !')

# ini = int(input(f'INICÍO: ').strip())
# fim = int(input(f'FIM: ').strip())
# passo = int(input(f'PASSO: ').strip())

# if ini > fim:    
#     passo = (passo - (passo+passo))

# contador(ini, fim, passo)



#Tentativa com while

# Executa a contagem definida pelo exercício.
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}.')

    if p < 0: #numero negativo
        p *= -1 #(Estou jogando o P para positivo)

    if p == 0: # se o passo for 0
        p = 1 # Passo 0 n existe vou deixar 1 pra ir de 1 em 1 
    
    #-Contador começa no I
    cont = i

    if i <= f:
    #-Enquanto o contador for menor q F
        while cont <= f:        
            print(f' |{cont}|', end=' ')#-Imprima o número
            cont += p #-Contador recebe cont + 1 (Agora o cont vale 2 e volta para inicio do laço)
        print()
        print('-='*30)
    else:
        while cont >= f:
            print(f' |{cont}|', end=' ')
            cont -= p
        print()
        print('-='*30)    



# Programa Principal 


#-C) Uma contagem persanolizada.
 #-A) de 1 até 10, de 1 em 1
contador(1, 10, 1)


#-B) de 10 até 0, de 2 em 2
contador(10, 0, 2)

print(f'Sua vez de personalizar uma contagem !')

ini = int(input(f'INICÍO: ').strip())
fim = int(input(f'FIM: ').strip())
passo = int(input(f'PASSO: ').strip())

contador(ini, fim, passo)