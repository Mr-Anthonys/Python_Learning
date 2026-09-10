# Módulos e Pacotes em Python — Guia Completo

## Sumário
1. [O que é um módulo](#1-o-que-é-um-módulo)
2. [Importando módulos](#2-importando-módulos)
3. [Formas de importar](#3-formas-de-importar)
4. [Criando seu próprio módulo](#4-criando-seu-próprio-módulo)
5. [O que é um pacote](#5-o-que-é-um-pacote)
6. [O arquivo __init__.py](#6-o-arquivo-__init__py)
7. [Módulos da biblioteca padrão mais usados](#7-módulos-da-biblioteca-padrão-mais-usados)
8. [if __name__ == "__main__"](#8-if-__name__--__main__)
9. [Importação relativa vs absoluta](#9-importação-relativa-vs-absoluta)
10. [Boas práticas](#10-boas-práticas)
11. [Erros comuns](#11-erros-comuns)

---

## 1. O que é um módulo

Um módulo é simplesmente um arquivo `.py` contendo código Python (funções, classes, variáveis) que pode ser reutilizado em outros arquivos.

---

## 2. Importando módulos

```python
import math

print(math.sqrt(16))   # 4.0
print(math.pi)          # 3.141592653589793
```

---

## 3. Formas de importar

```python
# Importar o módulo inteiro
import math
print(math.sqrt(9))

# Importar apenas o necessário
from math import sqrt, pi
print(sqrt(9))
print(pi)

# Importar tudo (evite, polui o namespace)
from math import *

# Importar com apelido (alias) — muito comum em bibliotecas de dados
import numpy as np
import pandas as pd

# Apelido para um item específico
from math import sqrt as raiz_quadrada
print(raiz_quadrada(25))  # 5.0
```

---

## 4. Criando seu próprio módulo

Suponha um arquivo `utilidades.py`:

```python
# utilidades.py
def somar(a, b):
    return a + b

def saudacao(nome):
    return f"Olá, {nome}!"

PI = 3.14159
```

E em outro arquivo, no mesmo diretório:

```python
# main.py
import utilidades

print(utilidades.somar(2, 3))       # 5
print(utilidades.saudacao("Ana"))   # Olá, Ana!

# ou importando itens específicos
from utilidades import somar, PI
print(somar(1, 1))
```

---

## 5. O que é um pacote

Um pacote é uma pasta contendo vários módulos relacionados, organizados juntos. Estrutura de exemplo:

```
meu_projeto/
├── main.py
└── calculadora/
    ├── __init__.py
    ├── operacoes_basicas.py
    └── operacoes_avancadas.py
```

```python
# calculadora/operacoes_basicas.py
def somar(a, b):
    return a + b

# main.py
from calculadora import operacoes_basicas
print(operacoes_basicas.somar(2, 3))

# ou
from calculadora.operacoes_basicas import somar
print(somar(2, 3))
```

---

## 6. O arquivo __init__.py

Marca uma pasta como pacote Python (obrigatório em versões mais antigas; opcional, mas ainda recomendado, nas mais recentes). Pode ficar vazio ou conter código de inicialização do pacote.

```python
# calculadora/__init__.py
from .operacoes_basicas import somar
from .operacoes_avancadas import potencia

# Agora, no main.py, é possível fazer diretamente:
from calculadora import somar, potencia
```

---

## 7. Módulos da biblioteca padrão mais usados

```python
import math       # funções matemáticas
import random      # números aleatórios
import datetime    # datas e horas
import os          # interação com o sistema operacional
import sys         # parâmetros e funções do interpretador
import json        # leitura/escrita de JSON
import re          # expressões regulares
import time        # controle de tempo, pausas
import collections # estruturas de dados extras (Counter, defaultdict, namedtuple)

print(random.randint(1, 10))          # número aleatório entre 1 e 10
print(datetime.datetime.now())        # data e hora atuais
print(os.getcwd())                    # diretório atual
```

---

## 8. if __name__ == "__main__"

Controla o que roda apenas quando o arquivo é executado diretamente — e não quando é importado por outro módulo.

```python
# utilidades.py
def somar(a, b):
    return a + b

if __name__ == "__main__":
    # só executa se rodar "python utilidades.py" diretamente
    print("Testando o módulo...")
    print(somar(2, 3))
```

Se outro arquivo fizer `import utilidades`, o bloco dentro do `if __name__ == "__main__":` **não** será executado — só a definição da função fica disponível.

---

## 9. Importação relativa vs absoluta

```python
# Importação absoluta (a partir da raiz do projeto) — mais recomendada
from calculadora.operacoes_basicas import somar

# Importação relativa (dentro de um pacote, usando ponto)
# Dentro de calculadora/operacoes_avancadas.py:
from .operacoes_basicas import somar   # "." significa "mesmo pacote"
from ..outro_pacote import algo        # ".." sobe um nível
```

---

## 10. Boas práticas

- Um módulo deve ter responsabilidade única e bem definida (ex: `utilidades.py`, `validacoes.py`)
- Evite `from modulo import *` — dificulta saber de onde cada função veio
- Use aliases padrão da comunidade (`import numpy as np`, `import pandas as pd`)
- Sempre proteja código de execução direta com `if __name__ == "__main__":`
- Organize projetos maiores em pacotes, agrupando módulos relacionados

---

## 11. Erros comuns

1. **ModuleNotFoundError** — módulo não está no mesmo diretório ou não foi instalado (`pip install nome`).
2. **Importação circular** — dois módulos tentando se importar mutuamente, gera erro.
3. **Conflito de nomes** — criar um arquivo `math.py` no seu projeto, que "esconde" o módulo `math` da biblioteca padrão.
4. **Esquecer `__init__.py`** (em versões mais antigas do Python) fazendo a pasta não ser reconhecida como pacote.
5. **Confundir `from x import *`** com nomes já existentes no seu código, sobrescrevendo funções sem perceber.

---

## Resumo rápido (cheat sheet)

```python
# Importar
import modulo
from modulo import item
import modulo as apelido
from modulo import item as apelido

# Criar módulo: qualquer arquivo .py
# Criar pacote: pasta com __init__.py

# Executar só quando roda direto
if __name__ == "__main__":
    ...
```
