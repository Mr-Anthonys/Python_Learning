# ============================================================
# Exercício de tuplas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercício 2:
 
#Contando Elementos
#Dada a seguinte tupla de notas de alunos:
#notas = (8.5, 7.0, 9.0, 5.5, 7.0, 10.0, 7.0, 6.5)
#Escreva um código que exiba quantas vezes a nota 7.0 aparece na tupla.
#Escreva um código que mostre em qual posição (índice) a nota 10.0 está localizada.

notas = (8.5, 7.0, 9.0, 5.5, 7.0, 10.0, 7.0, 6.5)
print(notas)
print(f'A nota 7.0 aparece {notas.count(7.0)} vezes. ')
print(f'Nota 10.0 está na {notas.index(10.0)+1}º posição')# somei 1 ao index da tupla pois é exclusivo o ultimo numero
