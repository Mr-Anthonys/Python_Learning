# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio

#7. O Detetive de Números (Maior e Menor):
#Peça para o usuário digitar 5 números inteiros.
#No final, sem usar as funções max() e min()
#(faça na raça usando um laço for e if)
#descubra qual é o maior e qual é o menor número da lista.

lista_numeros = []
maior = menor = 0
for c in range(0, 3):
    lista_numeros.append(int(input(f'Digite o {c+1}º número: ')))
    if lista_numeros > maior:
        maior = lista_numeros
        

print(maior,lista_numeros )
