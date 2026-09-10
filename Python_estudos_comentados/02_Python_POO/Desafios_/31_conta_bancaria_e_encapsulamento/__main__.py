# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from ContaBancaria import ContaBancaria

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    conta_1 = ContaBancaria(123, "Guilherme", 3000, chave="123456")
#region
    #print(conta_1) # Saída -> Estado atual da conta {
                                                       # '_id': 123, 
                                                       # '_titular': 'Guilherme',
                                                       # '_ContaBancaria__saldo': 3000,
                                                       # '_ContaBancaria__hash': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'
                                                       #  }
#endregion
    
    conta_1.sacar(200)
if __name__ == "__main__":
    main()