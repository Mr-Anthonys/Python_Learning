# Redes de Computadores — Guia do Básico ao Avançado

## 1. Conceitos fundamentais

Uma **rede de computadores** conecta dispositivos para que troquem dados. Elementos-chave:

| Termo | Significado |
|---|---|
| **Host** | Qualquer dispositivo conectado à rede (PC, servidor, celular) |
| **IP** | Endereço lógico que identifica um dispositivo na rede |
| **MAC Address** | Endereço físico único da placa de rede |
| **Protocolo** | Conjunto de regras para comunicação (TCP, HTTP, DNS...) |
| **Porta** | Número que identifica um serviço/aplicação em um host (ex.: 80 = HTTP) |
| **Pacote** | Unidade de dados transmitida pela rede |

---

## 2. Modelo OSI (7 camadas)

| Camada | Nome | Função | Exemplos |
|---|---|---|---|
| 7 | Aplicação | Interface com o usuário/software | HTTP, FTP, DNS, SMTP |
| 6 | Apresentação | Formatação, criptografia | SSL/TLS, JPEG |
| 5 | Sessão | Gerencia sessões de comunicação | NetBIOS, RPC |
| 4 | Transporte | Entrega confiável ou rápida dos dados | TCP, UDP |
| 3 | Rede | Roteamento entre redes | IP, ICMP |
| 2 | Enlace | Comunicação entre dispositivos na mesma rede | Ethernet, switches, MAC |
| 1 | Física | Transmissão de bits (cabos, sinais) | Cabo, Wi-Fi |

**Modelo TCP/IP** (mais usado na prática) simplifica em 4 camadas: Aplicação, Transporte, Internet, Acesso à Rede.

---

## 3. Endereçamento IP

### IPv4
Formato: `192.168.1.1` (4 blocos de 0-255, 32 bits no total)

Faixas privadas (não roteáveis na internet):
| Faixa | Uso comum |
|---|---|
| `10.0.0.0 – 10.255.255.255` | Redes corporativas grandes |
| `172.16.0.0 – 172.31.255.255` | Redes médias |
| `192.168.0.0 – 192.168.255.255` | Redes domésticas |

`127.0.0.1` = **localhost** (a própria máquina).

### Máscara de sub-rede e CIDR
A máscara define qual parte do IP é "rede" e qual é "host".

| Notação CIDR | Máscara | Hosts disponíveis |
|---|---|---|
| `/24` | 255.255.255.0 | 254 |
| `/16` | 255.255.0.0 | 65.534 |
| `/8` | 255.0.0.0 | 16.777.214 |

Exemplo: `192.168.1.0/24` → rede de 192.168.1.1 até 192.168.1.254 (broadcast: .255)

### IPv6
Formato mais longo, criado para resolver o esgotamento de IPv4: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

---

## 4. TCP vs UDP

| Característica | TCP | UDP |
|---|---|---|
| Conexão | Orientado à conexão (handshake) | Sem conexão |
| Confiabilidade | Garante entrega e ordem | Não garante |
| Velocidade | Mais lento (overhead de controle) | Mais rápido |
| Uso típico | Navegação web, e-mail, transferência de arquivos | Streaming, VoIP, jogos, DNS |

**Three-way handshake do TCP:**
```
Cliente → SYN → Servidor
Cliente ← SYN-ACK ← Servidor
Cliente → ACK → Servidor
```

---

## 5. Portas comuns

| Porta | Protocolo/Serviço |
|---|---|
| 20/21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP (envio de e-mail) |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 445 | SMB (compartilhamento Windows) |
| 3306 | MySQL |
| 3389 | RDP (Área de trabalho remota) |
| 5432 | PostgreSQL |
| 8080 | HTTP alternativo (proxies, apps web) |

Portas de 0–1023 são "well-known" (privilegiadas); 1024–49151 são registradas; 49152–65535 são dinâmicas/privadas.

---

## 6. DNS (Domain Name System)

Traduz nomes de domínio (`google.com`) em endereços IP.

| Termo | Significado |
|---|---|
| **Registro A** | Aponta um domínio para um IPv4 |
| **Registro AAAA** | Aponta um domínio para um IPv6 |
| **Registro CNAME** | Aponta um domínio para outro domínio (alias) |
| **Registro MX** | Define servidores de e-mail do domínio |
| **Registro TXT** | Texto livre (usado em verificações, SPF, DKIM) |
| **Registro NS** | Define os servidores DNS autoritativos |

Fluxo de resolução: Cliente → Resolver (ISP) → Root DNS → TLD DNS (.com) → DNS Autoritativo → resposta com IP

---

## 7. DHCP

Protocolo que atribui IP automaticamente aos dispositivos na rede.

Fluxo **DORA**:
```
Discover  → cliente busca um servidor DHCP
Offer     → servidor oferece um IP
Request   → cliente solicita aquele IP
Acknowledge → servidor confirma a atribuição
```

---

## 8. Roteamento e dispositivos de rede

| Dispositivo | Função | Camada OSI |
|---|---|---|
| **Hub** | Repete sinal para todas as portas (obsoleto) | 1 |
| **Switch** | Encaminha dados baseado no MAC address | 2 |
| **Router (Roteador)** | Encaminha dados entre redes diferentes, baseado em IP | 3 |
| **Firewall** | Filtra tráfego com base em regras de segurança | 3/4 (ou 7, se for de aplicação) |
| **Access Point** | Fornece conexão Wi-Fi | 1/2 |
| **Modem** | Converte sinal digital ↔ analógico (ou fibra) para acesso à internet | 1 |

**NAT (Network Address Translation)**: permite que vários dispositivos com IP privado compartilhem um único IP público para acessar a internet.

---

## 9. Modelo cliente-servidor e HTTP

| Termo | Significado |
|---|---|
| **Cliente** | Quem solicita o serviço (ex.: navegador) |
| **Servidor** | Quem responde à solicitação |
| **Request/Response** | Ciclo de pedido e resposta do HTTP |

Métodos HTTP comuns:
| Método | Função |
|---|---|
| `GET` | Solicita dados |
| `POST` | Envia dados (cria recurso) |
| `PUT` | Atualiza um recurso inteiro |
| `PATCH` | Atualiza parcialmente um recurso |
| `DELETE` | Remove um recurso |

Códigos de status HTTP comuns:
| Código | Significado |
|---|---|
| 200 | OK |
| 301/302 | Redirecionamento |
| 400 | Requisição inválida |
| 401 | Não autenticado |
| 403 | Proibido (sem permissão) |
| 404 | Não encontrado |
| 500 | Erro interno do servidor |

---

## 10. VPN, Proxy e Túneis

| Termo | Função |
|---|---|
| **VPN** | Cria um túnel criptografado entre dois pontos, simulando estar em outra rede |
| **Proxy** | Intermediário entre cliente e servidor, pode filtrar, cachear ou anonimizar tráfego |
| **Proxy reverso** | Fica na frente de servidores, distribuindo requisições (ex.: Nginx, Cloudflare) |
| **SSH Tunneling** | Encaminha tráfego de forma criptografada através de uma conexão SSH |

---

## 11. Wi-Fi e segurança de redes sem fio

| Protocolo | Segurança |
|---|---|
| WEP | Obsoleto, facilmente quebrável |
| WPA | Melhor que WEP, mas com falhas conhecidas |
| WPA2 | Padrão por muitos anos, usa AES |
| WPA3 | Mais recente e seguro, resistente a ataques offline de dicionário |

---

## 12. Ferramentas úteis para diagnóstico

| Ferramenta | Função |
|---|---|
| `ping` | Testa conectividade básica (ICMP) |
| `traceroute` / `tracert` | Mostra o caminho (saltos) até um destino |
| `nslookup` / `dig` | Consulta DNS |
| `netstat` / `ss` | Mostra conexões e portas ativas |
| `nmap` | Escaneia portas e serviços de uma rede/host (ver arquivo de Segurança Ofensiva) |
| `wireshark` | Captura e analisa pacotes de rede em detalhe |
| `curl` / `wget` | Testa requisições HTTP diretamente |
| `speedtest-cli` | Testa velocidade da conexão |

---

## 13. Conceitos avançados

| Termo | Significado |
|---|---|
| **VLAN** | Segmenta uma rede física em redes lógicas separadas |
| **Subnetting** | Dividir uma rede em sub-redes menores para organização/segurança |
| **BGP** | Protocolo de roteamento entre grandes redes (ISPs, backbone da internet) |
| **QoS (Quality of Service)** | Prioriza certos tipos de tráfego na rede |
| **Load Balancer** | Distribui tráfego entre múltiplos servidores |
| **CDN** | Rede de servidores distribuídos geograficamente para entregar conteúdo mais rápido |
| **Latência** | Tempo que um pacote leva para ir e voltar (ida e volta = RTT) |
| **Jitter** | Variação na latência, crítico para VoIP/streaming |

---

## 14. Boas práticas e segurança básica

- Trocar credenciais padrão de roteadores/APs
- Usar WPA3 (ou WPA2 no mínimo) em redes Wi-Fi
- Segmentar redes (ex.: VLAN separada para IoT)
- Manter firmware de roteadores atualizado
- Usar firewall para restringir tráfego desnecessário
- Monitorar tráfego incomum com ferramentas como Wireshark

---

## 15. Próximos passos sugeridos

- Praticar captura e análise de pacotes com Wireshark
- Montar um laboratório de rede virtual (ex.: com VirtualBox/GNS3) para testar roteamento e sub-redes
- Estudar subnetting na prática (calcular sub-redes manualmente)
- Seguir para os arquivos de **Segurança Ofensiva e Defensiva**, que usam esses conceitos de rede como base
