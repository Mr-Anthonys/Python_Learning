# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio 8.

#O Dobro e a Metade: Peça para o usuário digitar 5 números.
#Guarde-os em uma lista_original. 
#Depois, crie uma lista_resultado onde os números nas posições pares serão multiplicados por 2
#e os das posições ímpares serão divididos por 2.

lista_original = []
lista_resultado = []

for item in range(1, 6):#Entrada de dados com validação
    while True:
        entrada = input(f'Digite o {item}º número: ').strip().replace(',', '.')#Entrada STR removendo a , e colocando .

        
        if entrada.replace('.', '', 1).isdigit():#Transformando entrada em INTEIRO (removendo o . colocando ''(espaço vazio) pegando apenas o 1 (.)
            lista_original.append(float(entrada))#Lista aprende o numero STR castando para FLOAT
            break#Interrompe o laço
        else:#se n for numero: 
            print('Entrada inválida! Digite apenas números.')


for indice, valor in enumerate(lista_original):#Achando os indices com o enumerate
    if indice % 2 == 0:#se o indice (posição) for PAR
        lista_resultado.append(valor * 2)#Lista de resultado ja mutiplica por 2 se for PAR
    else:
        lista_resultado.append(valor / 2)#Lista de resultado ja divide se for IMPAR

# 3. Exibição dos resultados formatados
print('\n' + '='*30)
print(f'Lista Original:  {lista_original}')

# Criando uma exibição mais bonita para a lista de resultados (com 2 casas decimais)
lista_formatada = [f"{num:.2f}" for num in lista_resultado]
print(f'Lista Resultado: {lista_formatada}')
print('='*30)
        

