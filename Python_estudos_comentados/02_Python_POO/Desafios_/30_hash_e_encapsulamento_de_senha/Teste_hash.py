# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# HASH = Bagunça ou embaralhamento.
# SHA = Secure Hash Algorithm.

import hashlib

texto = "Importação"

texto_codificado = texto.encode('utf-8') # Estou encodando a string "Importação" em utf-8 (acentos, ç,  e por ai vai)
print(texto_codificado) # Saída sem passar pela hashlib.sha1 -> b'Importa\xc3\xa7\xc3\xa3o'

                    
# Lembrete que no momento de hoje 2026 é melhor usar o sha256 pra cima, pois os anterirores ja foram descriptografados...


hash = hashlib.sha1(texto_codificado).hexdigest() # Criando uma variavél hash e pegando o conteudo do texto codificado
                                                  # E criptografando pelo modo sha1
                                                  # Exibindo de maneira hexadecimal digitos de 0 até f (hexdigest())

print(hash) # Saída passando pela hashlib.sha1 -> 434b3fa450ddb3ebb3b7bc07b85d70144c7a4f76