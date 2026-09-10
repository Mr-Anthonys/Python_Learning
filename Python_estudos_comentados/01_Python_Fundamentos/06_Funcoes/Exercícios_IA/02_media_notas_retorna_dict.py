# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# # # Exercício 2 - Média de Notas
# # # Crie uma função calcular_media() que receba uma lista de notas.
# # # Ela deve retornar:
# # # * média
# # # * maior nota
# # # * menor nota
# # # Exemplo:
# # # Teste utilizando pelo menos cinco notas.
# # # Notas:
# # # 8
# # # 10
# # # 6
# # # 7
# # # 9
# # # Resultado:
# # # Média: 8.0
# # # Maior nota: 10
# # # Menor nota: 6



# # def calcular_media(* valores, l=None):
# #     """Calcular média, maior, menor valor informados e salvos em uma lista
     
# #         Args:
# #             Qualquer valor informado será salvo em uma tupla, l=None (para castar em lista depois)

# #         Return:
# #             maior, menor e media dos valores informados.           
# #         """
    
# #     if l == None:
# #         l = []
# #     l.append(valores)
# #     print(f'Notas informadas.')
# #     print('-='*20)
# #     for c in l:
# #         print(f' {c}', end=' ')
# #     print()

# #     #- Por usar o desempacotamento os valores são inseridos em uma TUPLA,
# #     #- o Exercício pede uma lista, então preciso verificar a tupla dentro da lista(indice[0])
# #     maior = max(l[0])
# #     menor = min(l[0])
# #     media = sum(l[0]) / len(l[0])
# #     print(f'O maior nota informada: {maior}')
# #     print(f'Menor nota informada: {menor}')
# #     print(f'média: {media:.2f}')
# #     return l


# # calcular_media(6, 8, 1, 88, 0, -99)

# # Retornando tupla
# def calcular_media(lista_notas):
#     if not lista_notas:
#         return [], 0, 0, 0
    
#     maior = max(lista_notas)
#     menor = min(lista_notas)
#     media = sum(lista_notas) / len(lista_notas)
    
#     # Retorna a lista original + os 3 valores calculados
#     return lista_notas, media, maior, menor

# # Testando:
# notas = [8, 10, 6, 7, 9]
# lista, med, max_n, min_n = calcular_media(notas)

# print(f"Lista analisada: {lista}")
# print(f"Média: {med:.1f} | Maior: {max_n} | Menor: {min_n}")


# # - copia 

# def calcular_media(lista_notas):
#     """Calcula a média, a maior e a menor nota de uma lista.
     
#     Args:
#         lista_notas (list): Uma lista contendo as notas (float ou int).

#     Returns:
#         tuple: (média, maior_nota, menor_nota)
#     """
#     if not lista_notas:
#         return 0, 0, 0  # Evita erro de divisão por zero caso a lista esteja vazia
    
#     maior = max(lista_notas)
#     menor = min(lista_notas)
#     media = sum(lista_notas) / len(lista_notas)
    
#     return media, maior, menor

# # --- Testando a função com o exemplo do enunciado ---

# notas_teste = [8, 10, 6, 7, 9]

# # Chamamos a função passando a lista e desempacotamos o retorno
# media_final, maior_nota, menor_nota = calcular_media(notas_teste)

# # Exibindo o resultado formatado
# print("Notas informadas:", notas_teste)
# print('-=' * 15)
# print(f"Média: {media_final:.1f}")
# print(f"Maior nota: {maior_nota}")
# print(f"Menor nota: {menor_nota}")




# Retornando um dicionário 

# Calcula e retorna a média a partir dos valores recebidos.
def calcular_media(lista_notas):
    if not lista_notas:
        return {"lista": [], "media": 0, "maior": 0, "menor": 0}
        
    return {
        "lista_original": lista_notas,
        "media": sum(lista_notas) / len(lista_notas),
        "maior": max(lista_notas),
        "menor": min(lista_notas)
    }

# Testando:
resultado = calcular_media([8, 10, 6, 7, 9])

print(f"Notas analisadas: {resultado['lista_original']}")
print(f"Média obtida: {resultado['media']:.1f}")
print(f"Maior nota: {resultado['maior']}")



# #Tudo dentro da função 

# def calcular_media(lista_notas):
#     """Calcula a média, maior e menor nota de uma lista e exibe o relatório."""
    
#     # Validação simples para evitar erro caso a lista venha vazia
#     if not lista_notas:
#         print("Nenhuma nota foi informada.")
#         return lista_notas

#     # Como já recebemos uma lista direta, não precisamos de índices como lista_notas[0]
#     maior = max(lista_notas)
#     menor = min(lista_notas)
#     media = sum(lista_notas) / len(lista_notas)

#     # Exibindo o relatório completo diretamente na tela
#     print("Notas informadas:")
#     for nota in lista_notas:
#         print(nota)
    
#     print("-" * 20)
#     print(f"Resultado:")
#     print(f"Média: {media:.1f}")
#     print(f"Maior nota: {maior}")
#     print(f"Menor nota: {menor}")
#     print("-" * 20)

#     # Retorna a lista conforme sua ideia original
#     return lista_notas


# # --- Execução direta e limpa ---
# # Basta chamar a função passando a lista como parâmetro!
# calcular_media([8, 10, 6, 7, 9])



