# DirBrute Web

# 🔎 DirBrute Web

DirBrute Web é uma ferramenta simples e intuitiva, feita com **Python + Flask**, que permite realizar **força bruta de diretórios** em um site alvo diretamente pelo navegador.  
Você informa uma URL, e o sistema varre caminhos com base em uma wordlist para encontrar páginas ou pastas ocultas (como `/admin`, `/login`, `/api`, etc).

---

## 🚀 Funcionalidades

- Interface web com HTML + CSS
- Scanner de diretórios baseado em wordlist
- Integração com o módulo `requests`
- Retorno dos status HTTP encontrados
- Detecção de páginas válidas diferentes de 404
- Totalmente personalizável

---

## 🧰 Requisitos

Antes de começar, instale:

- Python 3.8+
- Pip (gerenciador de pacotes Python)

---

## 📦 Instalação

1. **Clone ou baixe o projeto**:
   ```bash
   git clone https://github.com/seu-usuario/dirbrute-web.git
   cd dirbrute-web

2. Crie um ambiente virtual (opcional, mas recomendado):
  python -m venv venv
  venv\Scripts\activate  # Windows
  source venv/bin/activate  # Linux/macOS

3. Instale as dependências (no bash):
  pip install flask requests

🗂️ **Estrutura do Projeto**

  dirbrute-web/
      │
      ├── app.py                    # Código principal em Python (Flask)
      ├── wordlists.txt             # Wordlist com caminhos a testar
      ├── templates/
      │   ├── index.html            # Página inicial (formulário)
      │   └── resultado.html        # Página que mostra os resultados
      ├── static/
      │   └── style.css             # Estilos CSS para as páginas
      └── README.md                 # Com as intruções de funcionalidade

🛠️ **Como Usar**
  1. Certifique-se de que está na pasta correta.

  2. Execute o servidor Flask:
    python app.py
  
  3. Acesse no navegador:
    http://localhost:5000
    
  4. No campo "URL alvo", digite a URL do site que deseja escanear, por exemplo:
    https://exemplo.com
  
  5. Clique em "Iniciar Scan".
    O sistema vai varrer os caminhos definidos no arquivo wordlists.txt e mostrar quais retornam códigos HTTP válidos (exceto 404).

  ⚠️⚠️ ***Aviso Legal*** ⚠️⚠️
    *Este projeto é fornecido apenas para uso educacional e testes em sistemas autorizados.
     Nunca use essa ferramenta contra sistemas que você não tem permissão para testar.*

📌 **Autora**
Desenvolvido por **Beatriz Mandim**
Contato: [beatrizjuliomandim@gmail.com]

