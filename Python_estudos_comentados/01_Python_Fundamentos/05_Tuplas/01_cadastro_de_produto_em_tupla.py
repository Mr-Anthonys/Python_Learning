# ============================================================
# Exercício de tuplas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Exercício 1:

# Informações de Cadastro
# Crie uma tupla chamada produto que contenha o nome de um produto
# Preço (float) e a quantidade em estoque (int).
# Depois, utilize o desempacotamento para salvar cada valor em uma variável correspondente
# E exiba uma frase formatada na tela, 
# por exemplo: "O produto X custa R$ Y e temos Z unidades no estoque."

produto = ('Coca Cola', 11.50, 2)
preço = produto[1]
estoque = produto[2]
print(f'O produto "{produto[0]}" custa R$:{preço:.2f} e temos {estoque} no estoque.')
