# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#- Função chamada maior(), receba vaários parâmetros com valores inteiros
# - Analisar TODOS os valores e informar qual é o MAIOR.

# def maior(*valores):
#     maior = 0
#     for n in valores[0]:
#         if n == 0:
#             maior = menor = n

#         if n > maior:            
#             maior = n
        

#     print(f'Valores analisados --> {valores}\nMAIOR: {maior}')




# valores=[]
# cont = 0
# r = ' '
# while True:
#     valores.append(int(input(f'Informe o {cont+1}º VALOR: ')))
#     cont+=1
#     r = input('CONTINUAR? [S/N]: ').strip().upper()[0]
#     if r == 'N':
#         break

# maior(valores)

from time import sleep

# Analisa os valores recebidos para identificar o maior.
def maior(* valores):
    cont = maior = 0
    print('Analisando os valores informados...')
    for n in valores:
        print(f' {n}', end=' ', flush=True)#Flush=True para tirar o buffer/atraso        
        sleep(0.5)        
        if cont == 0:
            maior = n
        else:    
            if n > maior:
                maior = n
        cont += 1

        
    print(f'Foi informado {cont} valores.')
    print(f'O maior valor informado foi {maior}')


# - Programa principal 

maior(1, -6, 7)