# ============================================================
# Exercício de laços de repetição
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercício 3:

#Contagem de PAR e IMPAR
#leia 10 números  e no final mostre QUANTOS são pares e impares

lista_numeros = list()# Lista vazia
lista_par = list()
lista_impar = list()


for n in range(1 , 11):#Laço de 1 a 10
    while True:#laço infinito
        entrada = input(f'Informe o {n}º número inteiro: ').strip()#Entrada do valor.
        if entrada.isdigit():#Verificar se o input() informado foi somente números.
            numero = int(entrada)#VAriavél numero = entrada convertida para INT
            lista_numeros.append(numero)#Salva o valor convertido para int dentro da lista
            break # Termina o laço infinito
        else:#Se não for isdigit(númerico)
            print(f'O valor: "{entrada}" não é um número.\nInforme novamente !')
print('Ok vamos anlizar a quantidade de PARES e IMPARES dos valores informados.')

for valor in lista_numeros:#Para cada valor informado dentro da lista faça:
    #verificar quem é par
    if valor % 2 == 0:#Se o resto da divisão por 2 for = a 0 siginifa PAR.
        lista_par.append(valor)# Se for par, adiciona na lista do PAR
    else:#se não é par...
        lista_impar.append(valor)

# Resuldados
print(f'Valores informados são: {lista_numeros}')
print(f'Foi informado {len(lista_par)} números PARES.\n PARES >>>> {lista_par}')
print(f'Foi informado {len(lista_impar)} números ÍMPARES.\n ÍMPARES >>>> {lista_impar}')
