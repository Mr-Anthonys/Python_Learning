# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio 1.

# O Inversor de Nomes: Crie um programa que peça o nome de 5 pessoas
# guarde-os em uma lista e, no final, mostre os nomes na ordem inversa em que foram digitados.

nomes = []
for v in range(1, 6):
    nomes.append(input(f'Informe o {v}º NOME: ').strip().capitalize())

print(f'Nomes informados {nomes}.')
nomes.reverse()#Invertendo os nomes
print(f'Nomes com a ordem invertida: {nomes}')

