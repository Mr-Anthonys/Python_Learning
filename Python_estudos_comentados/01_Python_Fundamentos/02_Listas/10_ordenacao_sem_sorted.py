# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#ExercicioGuanabara
#region
#Leia 5 valores númerios e cadastre em uma lista, jána posição correta de inserção (sem o SORT())

lista = []#lista vazia
for c in range(0, 4):#Laço até 5 valores
    n = int(input('Informe um valor: '))#Entrada
    if c == 0:# se for o primeiro valor (indice 0)        
        lista.append(n)
    elif n > lista[-1]:#Se a entrada for maior q o ultimo elemento da lista
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):#Enquanto a pos for menor que o tamanho da lista
            if n <= lista[pos]:#Verificar se o N é menor ou igual do indice 
                lista.insert(pos, n)
               
                break
            pos =+ 1

print(f'Os valores digitados foram {lista}')
