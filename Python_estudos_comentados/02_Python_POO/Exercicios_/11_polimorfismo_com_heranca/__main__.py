# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from classes import * 

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():

    ancestral = Animal("Lucy")
    a = Gato("Zoro")
    b = Cachoro("Blaize")
    c = Galinha("pinTadinhA")
    d = Pato("DonalDs")




    cachorro_pequeno = CachorroPequeno("XuAua")
    cachorro_grande = CachorroGrande("BRUTUS")

    ancestral.emitir_som()
    a.emitir_som()
    b.emitir_som()
    c.emitir_som()
    d.emitir_som()

    cachorro_pequeno.emitir_som()
    cachorro_grande.emitir_som()

if __name__ == "__main__":
    main()