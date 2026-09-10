# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio 4.

#Leia Quantos jogos serão feitos.
#Sorteie 6 numeros "entre 1 a 60" para cada jogo, 
#Cadastrando TUDO em uma lista composta.

from random import randint


lista_numeros_temp = []
lista_final = []

print('='*30)
print(f'{"JOGOS MEGA-SENA":^30}')
print('='*30)

quantidade = int(input(f'Informe a quantidade de jogos: '))
for c in range(0,quantidade):
    while len(lista_numeros_temp) <= 5:
        num = randint(1,60)
        if num not in lista_numeros_temp:
            lista_numeros_temp.append(num)
    lista_final.append(lista_numeros_temp[:])
    lista_numeros_temp.clear() 
    
print('='*30)
print(f'{"Jogos Gerados":^30}')
print()

tot = 0
for jogo in lista_final:
    tot += 1
    jogo_str = map(str, sorted(jogo))#
    print('='*40)
    print(f'{tot}º JOGO ---> {"|".join(jogo_str)}')
print('='*40)
