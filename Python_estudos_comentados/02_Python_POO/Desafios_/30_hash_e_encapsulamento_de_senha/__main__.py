# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from Credencial import * 

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    c = Credencial()
    c.senha = '1234'         # Nada me impede de pedir um input para receber a senha ! 
    c.validar_senha("1234")  # Comparação das 2 hash da True
    c.validar_senha("12389") #                      da False

if __name__ == "__main__":
    main()