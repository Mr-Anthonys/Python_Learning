# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio 2.

#Limpando a Lista: Crie uma lista com 8 números inteiros digitados pelo usuário.
#Se o usuário digitar um número negativo, o programa deve ignorá-lo e não adicioná-lo à lista.
#Ao final, mostre a lista resultante.

lista_numeros = []#Lista

for item in range(1 , 9):#laço p/ 8 entradas
    while True:#laço p/ verificação da entrada
        entrada_numeros_str = input(f'Informe o {item}º número inteiro: ')#Entrada STR
        if entrada_numeros_str.isdigit(): #Se a entrada for numero            
            entrada_numeros_int = int(entrada_numeros_str)#Castando STR para INT
            if entrada_numeros_int >= 0:#se a entrada for positiva
                lista_numeros.append(entrada_numeros_int)#Valor da entrada vai para lista(sem os negativos)
            break# finaliza o laço de verificação
        else:#errou a resposta
            print(f'Resposta inválida. {entrada_numeros_str} não é um número inteiro.')
print(f'Lista e números desconsiderando os negativos ---> {lista_numeros}')


# FEITO POR IA 
# lista_numeros = []

# for item in range(1, 9):
#     entrada = input(f'Informe o {item}º número inteiro: ').strip()
    
#     # Validação: remove o "-" se existir, só para checar se o resto são dígitos
#     if entrada.replace('-', '', 1).isdigit():
#         numero_int = int(entrada)
        
#         if numero_int >= 0:
#             lista_numeros.append(numero_int)
#         else:
#             print(f'O número {numero_int} é negativo e foi ignorado.')
            
#     else:
#         print(f'"{entrada}" não é um número inteiro válido.')
# print(f'\nLista resultante (sem os negativos): {lista_numeros}')
#endregion