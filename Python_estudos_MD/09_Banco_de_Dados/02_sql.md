# SQL — Guia do Básico ao Avançado

## 1. O que é SQL

**SQL** (Structured Query Language) é a linguagem padrão para consultar e manipular bancos de dados relacionais (organizados em tabelas). Usada por MySQL, PostgreSQL, SQL Server, SQLite, Oracle, entre outros — a sintaxe base é parecida, com pequenas variações entre eles.

Categorias de comandos:
| Categoria | Sigla | Função |
|---|---|---|
| Data Query Language | DQL | Consultar dados (`SELECT`) |
| Data Manipulation Language | DML | Inserir, atualizar, apagar dados (`INSERT`, `UPDATE`, `DELETE`) |
| Data Definition Language | DDL | Criar/alterar estrutura (`CREATE`, `ALTER`, `DROP`) |
| Data Control Language | DCL | Permissões (`GRANT`, `REVOKE`) |
| Transaction Control Language | TCL | Transações (`COMMIT`, `ROLLBACK`) |

---

## 2. Criando estrutura (DDL)

```sql
CREATE DATABASE loja;

USE loja;

CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    idade INT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

| Comando | Função |
|---|---|
| `CREATE TABLE` | Cria uma tabela |
| `ALTER TABLE` | Modifica a estrutura de uma tabela existente |
| `DROP TABLE` | Apaga uma tabela (e todos os dados!) |
| `TRUNCATE TABLE` | Apaga todos os dados, mantendo a estrutura |

```sql
ALTER TABLE clientes ADD COLUMN telefone VARCHAR(20);
ALTER TABLE clientes DROP COLUMN telefone;
ALTER TABLE clientes MODIFY COLUMN idade SMALLINT;
```

### Tipos de dados comuns
| Tipo | Uso |
|---|---|
| `INT` | Números inteiros |
| `DECIMAL(10,2)` | Números decimais precisos (ex.: dinheiro) |
| `VARCHAR(n)` | Texto de tamanho variável, até n caracteres |
| `TEXT` | Texto longo |
| `DATE` | Data (YYYY-MM-DD) |
| `DATETIME` / `TIMESTAMP` | Data e hora |
| `BOOLEAN` | Verdadeiro/falso |

### Constraints (restrições)
| Constraint | Função |
|---|---|
| `PRIMARY KEY` | Identificador único da linha |
| `FOREIGN KEY` | Referencia outra tabela (integridade referencial) |
| `NOT NULL` | Campo obrigatório |
| `UNIQUE` | Valor não pode se repetir |
| `DEFAULT` | Valor padrão se nada for informado |
| `CHECK` | Valida uma condição (ex.: `CHECK (idade >= 0)`) |

---

## 3. Inserindo, atualizando e apagando dados (DML)

```sql
INSERT INTO clientes (nome, email, idade) VALUES ('Ana Silva', 'ana@email.com', 28);

INSERT INTO clientes (nome, email, idade) VALUES
    ('Bruno Costa', 'bruno@email.com', 35),
    ('Carla Dias', 'carla@email.com', 22);

UPDATE clientes SET idade = 29 WHERE nome = 'Ana Silva';

DELETE FROM clientes WHERE id = 3;
```

⚠️ **Nunca rode `UPDATE` ou `DELETE` sem `WHERE`** — isso afeta a tabela inteira.

---

## 4. Consultas básicas (SELECT)

```sql
SELECT * FROM clientes;
SELECT nome, email FROM clientes;
SELECT * FROM clientes WHERE idade > 25;
SELECT * FROM clientes ORDER BY nome ASC;
SELECT * FROM clientes ORDER BY idade DESC LIMIT 5;
SELECT DISTINCT idade FROM clientes;
```

| Cláusula | Função |
|---|---|
| `WHERE` | Filtra linhas |
| `ORDER BY` | Ordena resultado |
| `LIMIT` | Limita quantidade de linhas retornadas |
| `DISTINCT` | Remove duplicatas |
| `AS` | Renomeia coluna/tabela (alias) |

---

## 5. Operadores de filtro

| Operador | Função | Exemplo |
|---|---|---|
| `=`, `!=`, `>`, `<`, `>=`, `<=` | Comparação | `idade >= 18` |
| `AND` / `OR` / `NOT` | Lógicos | `idade > 18 AND cidade = 'SP'` |
| `BETWEEN` | Intervalo | `idade BETWEEN 18 AND 30` |
| `IN` | Lista de valores | `cidade IN ('SP', 'RJ')` |
| `LIKE` | Padrão de texto | `nome LIKE 'A%'` (começa com A) |
| `IS NULL` / `IS NOT NULL` | Verifica nulo | `email IS NULL` |

Curingas do `LIKE`: `%` (qualquer sequência), `_` (um caractere qualquer).

---

## 6. Funções agregadas e agrupamento

```sql
SELECT COUNT(*) FROM clientes;
SELECT AVG(idade) FROM clientes;
SELECT MAX(idade), MIN(idade) FROM clientes;
SELECT SUM(valor) FROM pedidos;

SELECT cidade, COUNT(*) AS total
FROM clientes
GROUP BY cidade;

SELECT cidade, COUNT(*) AS total
FROM clientes
GROUP BY cidade
HAVING COUNT(*) > 10;
```

| Função | Função |
|---|---|
| `COUNT()` | Conta linhas |
| `SUM()` | Soma valores |
| `AVG()` | Média |
| `MAX()` / `MIN()` | Maior/menor valor |
| `GROUP BY` | Agrupa linhas por uma coluna |
| `HAVING` | Filtra grupos (usado depois de `GROUP BY`, diferente do `WHERE`) |

---

## 7. Joins (junções entre tabelas)

Considerando `clientes(id, nome)` e `pedidos(id, cliente_id, valor)`:

```sql
-- INNER JOIN: só retorna linhas que têm correspondência nas duas tabelas
SELECT clientes.nome, pedidos.valor
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;

-- LEFT JOIN: retorna todos os clientes, mesmo sem pedidos (valor fica NULL)
SELECT clientes.nome, pedidos.valor
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;

-- RIGHT JOIN: retorna todos os pedidos, mesmo sem cliente correspondente
SELECT clientes.nome, pedidos.valor
FROM clientes
RIGHT JOIN pedidos ON clientes.id = pedidos.cliente_id;
```

| Tipo de Join | Retorna |
|---|---|
| `INNER JOIN` | Apenas registros com correspondência nas duas tabelas |
| `LEFT JOIN` | Todos da tabela da esquerda + correspondências da direita |
| `RIGHT JOIN` | Todos da tabela da direita + correspondências da esquerda |
| `FULL OUTER JOIN` | Todos os registros de ambas (nem todo banco suporta nativamente) |

---

## 8. Subqueries (subconsultas)

```sql
SELECT nome FROM clientes
WHERE id IN (SELECT cliente_id FROM pedidos WHERE valor > 500);

SELECT nome,
    (SELECT COUNT(*) FROM pedidos WHERE pedidos.cliente_id = clientes.id) AS total_pedidos
FROM clientes;
```

---

## 9. Relacionamentos entre tabelas

| Tipo | Exemplo |
|---|---|
| **1:1** (um-para-um) | Uma pessoa tem um passaporte |
| **1:N** (um-para-muitos) | Um cliente tem vários pedidos |
| **N:N** (muitos-para-muitos) | Alunos e cursos (precisa de tabela intermediária) |

Exemplo de N:N com tabela intermediária:
```sql
CREATE TABLE alunos (id INT PRIMARY KEY, nome VARCHAR(100));
CREATE TABLE cursos (id INT PRIMARY KEY, titulo VARCHAR(100));
CREATE TABLE alunos_cursos (
    aluno_id INT,
    curso_id INT,
    PRIMARY KEY (aluno_id, curso_id),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);
```

---

## 10. Transações (TCL)

Garantem que um conjunto de operações seja executado por completo ou não seja executado (atomicidade).

```sql
START TRANSACTION;

UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;

COMMIT;      -- confirma as mudanças
-- ou
ROLLBACK;    -- desfaz tudo se algo der errado
```

Propriedades **ACID**:
| Sigla | Significado |
|---|---|
| **A**tomicidade | Tudo ou nada |
| **C**onsistência | O banco sempre sai de um estado válido para outro |
| **I**solamento | Transações não interferem umas nas outras |
| **D**urabilidade | Uma vez confirmado, o dado persiste mesmo com falhas |

---

## 11. Índices (performance)

```sql
CREATE INDEX idx_email ON clientes(email);
DROP INDEX idx_email ON clientes;
```

Índices aceleram buscas (`WHERE`, `JOIN`, `ORDER BY`), mas custam espaço e deixam `INSERT`/`UPDATE` um pouco mais lentos — usar com critério, principalmente em colunas muito consultadas.

---

## 12. Views

Uma "tabela virtual" baseada em uma query salva.

```sql
CREATE VIEW clientes_sp AS
SELECT * FROM clientes WHERE cidade = 'SP';

SELECT * FROM clientes_sp;
```

---

## 13. Normalização (avançado)

Processo de organizar tabelas para reduzir redundância:

| Forma Normal | Regra principal |
|---|---|
| **1FN** | Cada célula tem um único valor atômico (sem listas dentro de uma coluna) |
| **2FN** | Atende 1FN + todo campo depende da chave primária inteira |
| **3FN** | Atende 2FN + nenhum campo depende de outro campo que não seja a chave |

Às vezes é feita a **desnormalização** propositalmente, trocando um pouco de redundância por performance de leitura.

---

## 14. Segurança: SQL Injection

Um dos ataques mais comuns contra aplicações web mal construídas — acontece quando entradas do usuário são concatenadas diretamente numa query.

```sql
-- Vulnerável (NUNCA fazer isso):
"SELECT * FROM usuarios WHERE email = '" + input + "'"

-- Um input malicioso como:  ' OR '1'='1
-- transforma a query em:  SELECT * FROM usuarios WHERE email = '' OR '1'='1'
-- retornando todos os usuários, ignorando o filtro
```

**Prevenção:** sempre usar *prepared statements* / *parameterized queries*, nunca concatenar strings vindas do usuário diretamente na query.

```python
# Exemplo seguro em Python (com sqlite3)
cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
```

---

## 15. Boas práticas

- Sempre use `WHERE` em `UPDATE`/`DELETE`
- Nomeie tabelas e colunas de forma clara e consistente
- Normalize o banco, mas sem exagerar (avalie performance também)
- Use índices em colunas muito consultadas, mas não em todas
- Use transações para operações que precisam ser atômicas
- Nunca monte queries por concatenação de strings com input do usuário

---

## 16. Próximos passos sugeridos

- Praticar joins combinando 3+ tabelas
- Montar um pequeno banco de dados relacional do zero (ex.: sistema de biblioteca)
- Estudar SQL Injection na prática, em ambiente controlado (ex.: DVWA), conectando com o arquivo de **Segurança Ofensiva**
- Explorar um SGBD específico (PostgreSQL ou MySQL) e suas particularidades
