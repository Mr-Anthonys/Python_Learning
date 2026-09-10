# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from Guan_Termostato import *

t = TermostatoGuana()
try:
    t.temperatura = 28.8
    

except Exception as e:
    print(f'Houve um problema : {e}')

finally:
    print(f"A temperatura atual é de {t.ftemperatura}")