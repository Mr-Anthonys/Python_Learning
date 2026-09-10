# Manipulação de arquivos CSV em Python

## Explicação informal

CSV é basicamente uma planilha em formato de texto puro: cada linha é uma linha da tabela, e as colunas são separadas por vírgula (ou ponto e vírgula). É o formato mais simples e universal para trocar dados tabulares — todo Excel, Google Sheets e banco de dados consegue exportar/importar CSV.

Python tem um módulo nativo `csv` que cuida dos detalhes chatos (aspas, separadores, quebras de linha) pra você.

## Explicação formal

CSV (Comma-Separated Values) é um formato de arquivo texto para dados tabulares, onde cada linha representa um registro e os valores são separados por um delimitador (geralmente vírgula `,` ou ponto e vírgula `;`). Python lida com CSV através do módulo nativo `csv`.

### Exemplo de arquivo `dados.csv`

```csv
nome,idade,cidade
Ana,28,São Paulo
Carlos,35,Rio de Janeiro
Beatriz,22,Curitiba
```

### Lendo um CSV — `csv.reader` (lista de listas)

```python
import csv

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

# ['nome', 'idade', 'cidade']
# ['Ana', '28', 'São Paulo']
# ['Carlos', '35', 'Rio de Janeiro']
# ['Beatriz', '22', 'Curitiba']
```

Repare que cada linha vira uma **lista de strings** — inclusive a primeira, que é o cabeçalho. Todos os valores vêm como `str`, mesmo os números.

### Lendo um CSV — `csv.DictReader` (lista de dicionários)

Geralmente mais prático, porque usa o cabeçalho como chave:

```python
import csv

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha)
        print(linha["nome"], linha["idade"])

# {'nome': 'Ana', 'idade': '28', 'cidade': 'São Paulo'}
# Ana 28
```

### Escrevendo um CSV — `csv.writer`

```python
import csv

pessoas = [
    ["nome", "idade", "cidade"],
    ["Ana", 28, "São Paulo"],
    ["Carlos", 35, "Rio de Janeiro"],
]

with open("saida.csv", "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(pessoas)   # grava todas as linhas de uma vez
    # ou: escritor.writerow(["Ana", 28, "São Paulo"]) para uma linha por vez
```

> **Atenção**: sempre use `newline=""` ao abrir o arquivo para escrita de CSV no Windows. Sem isso, o módulo `csv` pode gerar linhas em branco extras entre os registros.

### Escrevendo um CSV — `csv.DictWriter`

Útil quando seus dados já estão em dicionários (ex: vindos de uma lista de objetos):

```python
import csv

pessoas = [
    {"nome": "Ana", "idade": 28, "cidade": "São Paulo"},
    {"nome": "Carlos", "idade": 35, "cidade": "Rio de Janeiro"},
]

with open("saida.csv", "w", encoding="utf-8", newline="") as arquivo:
    campos = ["nome", "idade", "cidade"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()     # escreve a linha de cabeçalho
    escritor.writerows(pessoas)
```

### Delimitador diferente de vírgula

Em muitos países (incluindo o Brasil, no Excel local), o CSV usa `;` como separador, já que `,` é usado como separador decimal:

```python
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";")
    for linha in leitor:
        print(linha)
```

---

## Conteúdo bônus (extra — fora do escopo básico)

- **Conversão de tipos manual**: como o `csv` sempre lê tudo como string, se você precisar de números de verdade, precisa converter (`int(linha["idade"])`).
- **Módulo `pandas`**: para trabalhar com CSVs grandes ou fazer análises, `pandas.read_csv()` é muito mais poderoso que o módulo `csv` nativo (filtros, agregações, etc).
- **`csv.Sniffer`**: detecta automaticamente o delimitador usado em um arquivo CSV desconhecido.

```python
import csv

# Convertendo tipos ao ler (idade como int em vez de string)
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    pessoas = []
    for linha in leitor:
        linha["idade"] = int(linha["idade"])  # converte string -> int
        pessoas.append(linha)

maior_idade = max(pessoas, key=lambda p: p["idade"])
print(maior_idade)

# Detectando o delimitador automaticamente
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    amostra = arquivo.read(1024)
    dialeto = csv.Sniffer().sniff(amostra)
    print(f"Delimitador detectado: '{dialeto.delimiter}'")
```
