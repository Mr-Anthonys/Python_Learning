# ============================================================
# Exercício/rascunho de Python
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
cursos_oficiais = ["ADM", "ADS", "FISÍCA", "MEDICINA", "DEV"]

# Adiciona uma informação à estrutura de dados usada pelo objeto ou pelo exercício.
def add_curso(curso:str):
        curso = curso.strip().upper()
        if curso in cursos_oficiais:
             print(f"O Curso {curso} já está na LISTA DE CURSOS OFICIAIS.")

        elif 3 <= len(curso) <= 7:
            cursos_oficiais.append(curso)
        else:
            raise PermissionError(f"Curso {curso} não atende os requisitos para ser adicionado.")




add_curso("ADS")
add_curso("MONJARO")
print(cursos_oficiais)