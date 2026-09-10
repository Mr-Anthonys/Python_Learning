# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from Retangulo import Retangulo

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    r = Retangulo()
    try:
        r.base = 5
        r.altura = 12
        r.medidas = [8,9]        

    except Exception as error:
        print(f'Ocorreu um ERRO do tipo "{type(error).__name__}"\n{error}')

    print(r.medidas)

if __name__ == "__main__":
    main()