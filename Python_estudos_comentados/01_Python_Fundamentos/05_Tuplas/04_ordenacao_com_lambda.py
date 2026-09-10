# ============================================================
# Exercício de tuplas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercício 4: 

#Ordenação de Dados Estruturados
# Imagine que você recebeu uma lista de tuplas, onde cada tupla representa um aluno e sua respectiva nota final:
# alunos_notas = [("Ana", 8.2), ("Carlos", 9.5), ("Beatriz", 7.0), ("Daniel", 6.8)]
# Escreva um código que ordene essa lista de tuplas pela nota (do maior para o menor)
# Exibindo o ranking dos alunos na tela.
# (Dica: pesquise sobre o parâmetro key da função sorted() do Python ou o método .sort() de listas).

alunos_notas = [("Ana", 8.2), ("Carlos", 9.5), ("Beatriz", 7.0), ("Daniel", 6.8)]

ordernar_por_notas = sorted(alunos_notas, key=lambda x: x[1], reverse=True)

print(ordernar_por_notas)

