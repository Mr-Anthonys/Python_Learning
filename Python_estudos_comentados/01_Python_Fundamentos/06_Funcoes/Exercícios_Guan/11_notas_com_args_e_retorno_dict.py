# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# função notas() recebe varias notas e retorna um dicionário:
#qnt de notas
#menor e maior nota, media notas
#situação (opicional)
#docstrings


# Função/método responsável pela operação indicada pelo nome dentro deste exercício.
def notas(* valores, sit=False):
    """Recebe notas, verifica maior, menor, media, qnt , e situação.
    Args:
        qlqer qnt de notas + sit (se quiser ver a situação da media)
    Return:
        Dicionário com os valores"""
    

    dict_notas = {}
    dict_notas["quantidade"] = len(valores)
    dict_notas["maior"] = max(valores)
    dict_notas["menor"] = min(valores)
    dict_notas["media"] = sum(valores) / len(valores)
  # Se sit=True, adicionamos o campo 'situacao' DENTRO do dicionário
    if sit:
        if dict_notas["media"] < 5:
            dict_notas["situacao"] = "RUIM"
        elif dict_notas["media"] < 7:
            dict_notas["situacao"] = "RAZOÁVEL"
        else:
            dict_notas["situacao"] = "BOA" 

    return dict_notas

resultado = notas(1, 6, 88, 3 ,4,)

print(resultado)