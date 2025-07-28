from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    url = request.form["url"].strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    resultados = []

    try:
        with open("wordlists.txt", "r") as file:
            wordlist = file.readlines()
    except IOError:
        return "Erro: Não foi possível ler o arquivo wordlists.txt"

    for word in wordlist:
        palavra = word.strip()
        if not palavra:  # ignora linhas vazias
            continue
            
        url_final = f"{url}/{palavra}"
        try:
            response = requests.get(url_final, timeout=5)
            code = response.status_code
            if code != 404:
                resultados.append((url_final, code))
        except requests.exceptions.RequestException as e:
            resultados.append((url_final, f"Erro ao acessar: {str(e)}"))

    return render_template("resultado.html", resultados=resultados)
    
if __name__ == "__main__":
    app.run(debug=True)