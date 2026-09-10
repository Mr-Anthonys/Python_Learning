# Banco de Dados — Guia Básico (com foco em Python)

## Sumário
1. [O que é um banco de dados](#1-o-que-é-um-banco-de-dados)
2. [Banco relacional vs não-relacional](#2-banco-relacional-vs-não-relacional)
3. [Conceitos básicos de banco relacional](#3-conceitos-básicos-de-banco-relacional)
4. [SQL: comandos essenciais](#4-sql-comandos-essenciais)
5. [Conectando Python a um banco de dados](#5-conectando-python-a-um-banco-de-dados)
6. [Usando SQLite (mais simples para começar)](#6-usando-sqlite-mais-simples-para-começar)
7. [Evitando SQL Injection](#7-evitando-sql-injection)
8. [ORMs (SQLAlchemy)](#8-orms-sqlalchemy)
9. [Bancos NoSQL na prática (MongoDB)](#9-bancos-nosql-na-prática-mongodb)
10. [Boas práticas](#10-boas-práticas)
11. [Erros comuns](#11-erros-comuns)

---

## 1. O que é um banco de dados

Um sistema organizado para armazenar, consultar e gerenciar dados de forma persistente (diferente de variáveis, que somem quando o programa termina).

---

## 2. Banco relacional vs não-relacional

| Relacional (SQL) | Não-relacional (NoSQL) |
|---|---|
| Dados organizados em tabelas (linhas e colunas) | Dados em documentos, chave-valor, grafos, etc. |
| Estrutura fixa (schema definido) | Estrutura flexível |
| Exemplos: PostgreSQL, MySQL, SQLite, SQL Server | Exemplos: MongoDB, Redis, Cassandra |
| Bom para dados estruturados e relações complexas | Bom para dados flexíveis, grande escala |

---

## 3. Conceitos básicos de banco relacional

- **Tabela**: conjunto de dados organizados em linhas e colunas (ex: tabela `usuarios`)
- **Coluna (campo)**: um atributo do dado (ex: `nome`, `idade`)
- **Linha (registro)**: um item individual da tabela (ex: um usuário específico)
- **Chave primária (Primary Key)**: identificador único de cada linha (ex: `id`)
- **Chave estrangeira (Foreign Key)**: referência à chave primária de outra tabela, criando relacionamento

```
Tabela: usuarios
+----+---------+------+
| id | nome    | idade|
+----+---------+------+
| 1  | Ana     | 25   |
| 2  | Bruno   | 30   |
+----+---------+------+

Tabela: pedidos
+----+-------------+---------+
| id | usuario_id  | produto |
+----+-------------+---------+
| 1  | 1           | Livro   |
+----+-------------+---------+
```
`usuario_id` na tabela `pedidos` é uma chave estrangeira que referencia `id` na tabela `usuarios`.

---

## 4. SQL: comandos essenciais

SQL (Structured Query Language) é a linguagem usada para interagir com bancos relacionais.

```sql
-- Criar uma tabela
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
);

-- Inserir dados
INSERT INTO usuarios (nome, idade) VALUES ('Ana', 25);

-- Consultar dados
SELECT * FROM usuarios;
SELECT nome, idade FROM usuarios WHERE idade >= 18;
SELECT * FROM usuarios ORDER BY idade DESC;
SELECT * FROM usuarios LIMIT 10;

-- Atualizar dados
UPDATE usuarios SET idade = 26 WHERE nome = 'Ana';

-- Deletar dados
DELETE FROM usuarios WHERE nome = 'Ana';

-- Juntar tabelas relacionadas (JOIN)
SELECT usuarios.nome, pedidos.produto
FROM usuarios
JOIN pedidos ON usuarios.id = pedidos.usuario_id;
```

---

## 5. Conectando Python a um banco de dados

Python se conecta a bancos usando bibliotecas específicas para cada tipo:

| Banco | Biblioteca comum |
|---|---|
| SQLite | `sqlite3` (já vem no Python) |
| PostgreSQL | `psycopg2` |
| MySQL | `mysql-connector-python` |
| MongoDB | `pymongo` |

---

## 6. Usando SQLite (mais simples para começar)

SQLite não precisa de servidor — o banco fica salvo em um único arquivo. Ótimo para aprender e para projetos pequenos.

```python
import sqlite3

# Conectar (cria o arquivo se não existir)
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
""")

# Inserir dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Ana", 25))
conexao.commit()  # salva as alterações

# Inserir vários de uma vez
usuarios = [("Bruno", 30), ("Carla", 22)]
cursor.executemany("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", usuarios)
conexao.commit()

# Consultar dados
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()  # lista de tuplas
for linha in resultados:
    print(linha)

# Consultar um único resultado
cursor.execute("SELECT * FROM usuarios WHERE nome = ?", ("Ana",))
usuario = cursor.fetchone()
print(usuario)

# Fechar a conexão
conexao.close()
```

Usando `with` para fechar automaticamente:

```python
with sqlite3.connect("meu_banco.db") as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())
```

---

## 7. Evitando SQL Injection

**Nunca** monte queries SQL concatenando strings diretamente com dados do usuário — isso abre brecha para ataques de SQL Injection.

```python
# ERRADO — vulnerável a SQL Injection
nome = input("Nome: ")
cursor.execute(f"SELECT * FROM usuarios WHERE nome = '{nome}'")

# CORRETO — usa parâmetros (placeholders), o driver escapa os valores com segurança
nome = input("Nome: ")
cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))
```

---

## 8. ORMs (SQLAlchemy)

Um ORM (Object-Relational Mapping) permite trabalhar com o banco de dados usando classes e objetos Python, em vez de escrever SQL diretamente. `SQLAlchemy` é o mais usado no ecossistema Python.

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

engine = create_engine("sqlite:///meu_banco.db")
Base.metadata.create_all(engine)  # cria as tabelas

Session = sessionmaker(bind=engine)
sessao = Session()

# Inserir
novo_usuario = Usuario(nome="Ana", idade=25)
sessao.add(novo_usuario)
sessao.commit()

# Consultar
usuarios = sessao.query(Usuario).filter(Usuario.idade >= 18).all()
for u in usuarios:
    print(u.nome, u.idade)
```

---

## 9. Bancos NoSQL na prática (MongoDB)

MongoDB armazena dados como documentos (parecidos com JSON/dicionários Python), sem schema fixo.

```python
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
banco = cliente["meu_banco"]
colecao = banco["usuarios"]

# Inserir
colecao.insert_one({"nome": "Ana", "idade": 25})

# Consultar
usuario = colecao.find_one({"nome": "Ana"})
print(usuario)

for u in colecao.find({"idade": {"$gte": 18}}):
    print(u)
```

---

## 10. Boas práticas

- Sempre use parâmetros (`?` ou `%s`, dependendo do driver) em vez de concatenar strings — previne SQL Injection
- Feche conexões após o uso (ou use `with`)
- Use `commit()` após operações de escrita (INSERT/UPDATE/DELETE) — senão as mudanças não são salvas
- Para projetos pequenos/aprendizado, SQLite é suficiente; para produção, considere PostgreSQL/MySQL
- Considere um ORM (como SQLAlchemy) em projetos maiores, para código mais organizado e portável entre bancos

---

## 11. Erros comuns

1. **Esquecer o `commit()`** — a alteração fica só na sessão atual e não é salva no arquivo/banco.
2. **Concatenar strings para montar SQL** — abre brecha de segurança (SQL Injection).
3. **Não fechar a conexão** — pode causar problemas de acesso simultâneo, especialmente em SQLite.
4. **Confundir `fetchone()` com `fetchall()`** — o primeiro retorna um único resultado (ou `None`), o segundo retorna uma lista de todos os resultados.
5. **Não tratar exceções de conexão/consulta** — sempre bom envolver operações de banco em `try/except`.

---

## Resumo rápido (cheat sheet)

```python
import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS tabela (id INTEGER PRIMARY KEY, campo TEXT)")
cursor.execute("INSERT INTO tabela (campo) VALUES (?)", ("valor",))
conexao.commit()

cursor.execute("SELECT * FROM tabela")
print(cursor.fetchall())

conexao.close()
```

```sql
SELECT * FROM tabela WHERE condicao;
INSERT INTO tabela (coluna) VALUES (valor);
UPDATE tabela SET coluna = valor WHERE condicao;
DELETE FROM tabela WHERE condicao;
```
