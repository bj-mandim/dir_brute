<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
</div>

<br>

<div align="center">
  <h1>🛡️ DirBrute Web</h1>
  <p><strong>Laboratório de Auditoria Web: Reconhecimento de Infraestrutura e Diretórios Ocultos</strong></p>
</div>

---

## 🎯 O Propósito 

O **DirBrute Web** nasceu de uma necessidade clara: facilitar a fase de *Reconhecimento* em auditorias de segurança e testes de intrusão, unindo o poder e a flexibilidade das ferramentas de linha de comando (como DirBuster, ffuf e gobuster) com a usabilidade e agilidade de uma interface web moderna e intuitiva. 

Sob a ótica de **Offensive Security**, desenvolvemos este ambiente para remover barreiras técnicas imediatas — não é preciso decorar flags no terminal para realizar uma varredura rápida e descobrir ativos expostos em uma aplicação, como painéis administrativos (`/admin`), endpoints de API (`/api/v1`), arquivos de configuração vazados (`/wp-config.php.bak`) ou outras pastas ocultas.

## ⚙️ Tecnologias Utilizadas

A arquitetura do projeto foi pensada para ser leve, rodando de forma standalone com dependências mínimas, mas apresentando um visual "Premium Cybersecurity Mode" via Glassmorphism:

*   **Backend & Lógica**: `Python 3` + `Flask`
*   **Requisições HTTP**: Biblioteca `requests` (para lidar com timeouts, status codes e retentativas)
*   **Frontend**: `HTML5`, `Vanilla JavaScript` e um `CSS3` altamente customizado.
*   **Design**: Dark Mode / Cyber Tema (Acentos neon verde e azul, UI responsiva com *Glassmorphism*, tabelas stream-ready simuladas e console em tempo real).
*   **Animações**: Feedback visual contínuo através de animações CSS Keyframes, SVG radar e loading dots nativos.

---

## 🚀 Como Funciona?

O processo de exploração ocorre em três etapas fundamentais:

1.  **Definição do Alvo**: Através do dashboard central, você insere a URL (ex: `https://site.com`). A ferramenta realiza validações regex visuais em tempo real.
2.  **Ataque Baseado em Dicionário (Wordlist)**: O backend lê o arquivo `wordlists.txt` linha por linha, iterando sobre dezenas (ou milhares) de caminhos prováveis, disparando requisições *GET* para cada caminho construído (`url/palavra`).
3.  **Resultados Qualificados**: O fluxo finaliza renderizando todos os status codes distintos de `404 (Not Found)`. Códigos de sucesso (`200`), redirecionamentos (`301`, `302`), erros de autorização (`401`, `403`) e falhas internas do alvo (`500`) são exibidos em uma dashboard de análise equipada com *badges* semânticos e console dinâmico.

---

## 🖥️ Como rodar na sua máquina local

Para configurar o ambiente e começar a utilizar a ferramenta na sua máquina, siga os passos abaixo:

### Pré-requisitos
*   **Python 3.8** ou superior instalado e configurado no PATH.

### Passos para Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/dirbrute-web.git
   cd dirbrute-web
   ```

2. **(Opcional) Crie e ative um ambiente virtual:**
   Isto é altamente recomendado para não poluir o Python global da sua máquina.
   * **No Windows:**
     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```
   * **No Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências:**
   Com o ambiente ativado (ou não, caso tenha pulado o passo anterior), rode:
   ```bash
   pip install flask requests
   ```

4. **Inicie o Servidor:**
   ```bash
   python app.py
   ```
   *O console indicará que o Flask está rodando em `http://127.0.0.1:5000` (ou localhost).*

5. **Acesse e Use:**
   * Abra seu navegador preferido e acesse `http://localhost:5000`.
   * Insira a URL do alvo que deseja testar na tela principal.
   * *(Opcional): Se quiser testar rotas mais agressivas, adicione suas próprias palavras ao arquivo `wordlists.txt` que fica na raiz do projeto antes de iniciar o scan.*

---

## ⚠️ Aviso Legal e Responsabilidade

O **DirBrute Web** é fornecido rigorosamente para **USO EDUCACIONAL**, pesquisas de segurança da informação e testes em sistemas corporativos que você possui **autorização explícita** para auditar (como em programas de *Bug Bounty* verificados ou testes de penetração autorizados em contrato). 

> **O uso indevido contra alvos não autorizados ou redes públicas governamentais/privadas que não lhe pertencem é ilegal, imoral e não possui correlação com a autora do projeto.**

<br>

<div align="center">
  <sub>Desenvolvido com curiosidade e ♥ por <b>Beatriz Mandim</b> &middot; Contato: <a href="mailto:beatrizjuliomandim@gmail.com">beatrizjuliomandim@gmail.com</a></sub>
</div>
