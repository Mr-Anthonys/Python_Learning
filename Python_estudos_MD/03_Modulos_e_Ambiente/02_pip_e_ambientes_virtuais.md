# Bibliotecas Externas, pip e Ambientes Virtuais — Guia Completo

## Sumário
1. [O que são bibliotecas externas](#1-o-que-são-bibliotecas-externas)
2. [O que é o pip](#2-o-que-é-o-pip)
3. [Comandos essenciais do pip](#3-comandos-essenciais-do-pip)
4. [O que é um ambiente virtual e por que usar](#4-o-que-é-um-ambiente-virtual-e-por-que-usar)
5. [Criando e usando venv](#5-criando-e-usando-venv)
6. [requirements.txt](#6-requirementstxt)
7. [Verificando pacotes instalados](#7-verificando-pacotes-instalados)
8. [Bibliotecas populares por área](#8-bibliotecas-populares-por-área)
9. [pip vs conda](#9-pip-vs-conda)
10. [Boas práticas](#10-boas-práticas)
11. [Erros comuns](#11-erros-comuns)

---

## 1. O que são bibliotecas externas

Códigos escritos por terceiros (comunidade Python) que resolvem problemas comuns, para você não precisar "reinventar a roda". Diferente dos módulos da biblioteca padrão (`math`, `os`, etc.), essas precisam ser **instaladas** antes de usar.

```python
import pandas as pd  # biblioteca externa, precisa ser instalada com pip antes
```

---

## 2. O que é o pip

O **gerenciador de pacotes** padrão do Python — usado para instalar, atualizar e remover bibliotecas a partir do PyPI (Python Package Index), o repositório oficial.

```bash
pip --version   # verificar se está instalado e qual versão
```

---

## 3. Comandos essenciais do pip

```bash
# Instalar uma biblioteca
pip install requests

# Instalar uma versão específica
pip install requests==2.31.0

# Instalar a versão mínima
pip install requests>=2.25.0

# Atualizar uma biblioteca já instalada
pip install --upgrade requests

# Desinstalar
pip uninstall requests

# Listar tudo que está instalado
pip list

# Ver detalhes de uma biblioteca instalada
pip show requests
```

---

## 4. O que é um ambiente virtual e por que usar

Um ambiente virtual é um espaço **isolado** com sua própria instalação de Python e bibliotecas, separado do resto do sistema. Isso evita:

- Conflitos de versão entre projetos diferentes (um projeto precisa do Django 3, outro do Django 5)
- "Poluir" a instalação global do Python com dezenas de bibliotecas de projetos distintos
- Problemas ao compartilhar o projeto com outras pessoas (cada um usa seu próprio ambiente)

---

## 5. Criando e usando venv

`venv` é o módulo padrão do Python para criar ambientes virtuais (já vem instalado).

```bash
# Criar o ambiente virtual (cria uma pasta chamada "venv")
python -m venv venv

# Ativar o ambiente

# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate

# Depois de ativado, o terminal mostra algo como (venv) no início da linha,
# indicando que o ambiente está ativo

# Instalar bibliotecas DENTRO do ambiente ativo
pip install requests pandas

# Desativar o ambiente (volta ao Python global)
deactivate
```

> Enquanto o ambiente estiver ativo, tudo que for instalado com `pip install` fica isolado dentro dele — não afeta o sistema nem outros projetos.

---

## 6. requirements.txt

Arquivo que lista todas as bibliotecas (e versões) que um projeto precisa, facilitando compartilhar e recriar o ambiente em outra máquina.

```bash
# Gerar o arquivo com tudo que está instalado no ambiente atual
pip freeze > requirements.txt
```

Exemplo de conteúdo de `requirements.txt`:

```
requests==2.31.0
pandas==2.1.4
numpy==1.26.2
```

```bash
# Instalar todas as bibliotecas listadas no arquivo (em outra máquina/ambiente)
pip install -r requirements.txt
```

---

## 7. Verificando pacotes instalados

```bash
pip list                 # lista tudo instalado no ambiente atual
pip list --outdated      # mostra quais estão desatualizados
pip show nome_pacote     # detalhes: versão, dependências, localização
```

---

## 8. Bibliotecas populares por área

| Área | Bibliotecas comuns |
|---|---|
| Requisições web/APIs | `requests`, `httpx` |
| Análise de dados | `pandas`, `numpy` |
| Visualização de dados | `matplotlib`, `seaborn`, `plotly` |
| Machine Learning | `scikit-learn`, `tensorflow`, `pytorch` |
| Desenvolvimento web | `flask`, `django`, `fastapi` |
| Automação/scraping | `beautifulsoup4`, `selenium`, `scrapy` |
| Cyber-segurança | `scapy`, `paramiko`, `cryptography` |
| Banco de dados | `sqlalchemy`, `psycopg2`, `pymongo` |
| Testes | `pytest`, `unittest` (biblioteca padrão) |

```bash
pip install requests pandas matplotlib flask pytest
```

---

## 9. pip vs conda

`conda` é outro gerenciador de pacotes (vem com Anaconda/Miniconda), mais comum em ciência de dados, pois também gerencia versões do próprio Python e dependências não-Python (como bibliotecas em C).

| | pip | conda |
|---|---|---|
| Repositório | PyPI | Anaconda repository |
| Gerencia versão do Python | Não | Sim |
| Ambiente virtual | Precisa do `venv` separado | Já integrado (`conda create`) |
| Uso mais comum | Projetos gerais, web, automação | Ciência de dados, ambientes complexos |

---

## 10. Boas práticas

- Sempre crie um ambiente virtual por projeto — nunca instale tudo globalmente
- Gere e mantenha atualizado um `requirements.txt` para facilitar reprodução do ambiente
- Fixe as versões das bibliotecas em projetos importantes (`biblioteca==1.2.3`), evitando quebras inesperadas com atualizações
- Nomeie o ambiente virtual de forma clara ou use sempre o mesmo nome (`venv`) e adicione ao `.gitignore`
- Antes de instalar uma biblioteca desconhecida, verifique sua popularidade/manutenção no PyPI

---

## 11. Erros comuns

1. **Instalar bibliotecas sem ativar o ambiente virtual** — acaba instalando no Python global sem perceber.
2. **Esquecer de ativar o ambiente virtual** antes de rodar o projeto, causando `ModuleNotFoundError`.
3. **Subir a pasta do ambiente virtual (`venv/`) para o Git** — deveria ir para o `.gitignore`; o certo é compartilhar apenas o `requirements.txt`.
4. **Confundir `pip install` (temporário, na sessão do terminal) com adicionar ao `requirements.txt`** — instalar não atualiza o arquivo automaticamente, é preciso rodar `pip freeze` de novo.
5. **Misturar pip e conda no mesmo ambiente** sem cuidado, o que pode gerar conflitos de dependência.

---

## Resumo rápido (cheat sheet)

```bash
# Ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
deactivate

# pip
pip install nome_pacote
pip install nome_pacote==1.0.0
pip uninstall nome_pacote
pip list
pip show nome_pacote

# requirements.txt
pip freeze > requirements.txt
pip install -r requirements.txt
```
