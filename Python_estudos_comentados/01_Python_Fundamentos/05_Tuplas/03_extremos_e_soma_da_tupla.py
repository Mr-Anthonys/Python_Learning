# ============================================================
# Exercício de tuplas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercício 4:
 
# Análise de Extremos
# Crie uma tupla com 10 números inteiros quaisquer (positivos e negativos). 
# Escreva um programa que encontre e imprima:
# Maior número da tupla.
# O menor número da tupla.
# A soma de todos os elementos.
#Dica: o Python possui funções nativas como max(), min() e sum() que aceitam tuplas).

numeros = (-12, 2, 6, 12, 5, 22, 13, -7, 2, 10 )
print(f'O maior numero é {max(numeros)}')
print(f'O menor numero da tupla é {min(numeros)}')
print(f'A soma de todos os numeros da tupla é {sum(numeros)}')

