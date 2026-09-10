# ============================================================
# Exercício de laços de repetição
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercício 2:
#Leia 2 num do usuario(inicio e fim) e mostre a soma de todos os numeros. 

i = input('Informe um número para o inicio: ')
f = input('Informe um número para o final:  ')
i = int(i)
f = int(f)
soma = 0
for c in range(i, f+1):
    soma += c # MEsma coisa que (soma = soma + c)
print(f'A soma de todos os numéros é {soma}.')
