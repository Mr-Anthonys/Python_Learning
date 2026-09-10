# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from abc import ABC, abstractmethod

# Uma classe chamada ANIMAL (abstrata) q possui um metodo emitir_som()
# A classe `Animal` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Animal(ABC):
    def __init__(self, nome:str = '<Vazio>'):
        self.nome = nome

    # Método emitir_som() onde TODAS AS CLASSES que herdarem de ANIMAL irão SOBREESCREVER esse método alterando a funcionalidade
    def emitir_som(self):
        print(f'"{self.nome}" é {self.__class__.__name__}.\nE está emitindo um SOM !')

# A classe `Pato` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Pato(Animal):
    def emitir_som(self):
        print(f'Me chamo {self.nome.title()}, sou {self.__class__.__name__}, e estou dizendo "QUACK QUACK"')

# A classe `Cachoro` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Cachoro(Animal):
    def emitir_som(self):
        print(f'Me chamo {self.nome.title()}, sou {self.__class__.__name__}, e estou dizendo "AU AU AU"')

 # Uma sub-classe de Cachorro, representando um cachorro pequeno e outro grande.
# A classe `CachorroPequeno` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class CachorroPequeno(Cachoro):
    def emitir_som(self):
            print(f'Me chamo {self.nome.title()}, sou {self.__class__.__name__}, e estou dizendo "au au au au au au"')


# A classe `CachorroGrande` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class CachorroGrande(Cachoro):
    def emitir_som(self):
            print(f'Me chamo {self.nome.title()}, sou {self.__class__.__name__}, e estou dizendo "RUFH RUFH"')

        

# A classe `Gato` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Gato(Animal):
    def emitir_som(self):
        print(f'Me chamo {self.nome.title()}, sou {self.__class__.__name__}, e estou dizendo "MIAU MIAU"')

# A classe `Galinha` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Galinha(Animal):
    def emitir_som(self):
        print(f'Me chamo {self.nome.title()}, sou {self.__class__.__name__}, e estou dizendo "PÓ PÓ PÓ"')