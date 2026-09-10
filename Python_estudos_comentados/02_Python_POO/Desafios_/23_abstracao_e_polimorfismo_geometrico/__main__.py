# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from Poligonos import Quadrado, Circulo
# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    q = Quadrado(20)
    print(f'Um quadrado de lado {q.lado} tem perimétro de {q.perimetro()}')
    print(f"Um quadrado de lado {q.lado} tem área de {q.area()}m²")

    c = Circulo()
    print(f'Um Círculo de raio {c.raio}cm tem perimétro de {c.perimetro():.1f}cm')
    print(f'Um círculo de raio {c.raio}cm tem área de {c.area():.1f}cm')

if __name__ == "__main__":
    main()