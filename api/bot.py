from flask import Flask
import subprocess
import os

app = Flask(__name__)

BOT_PATH = os.path.join(os.getcwd(), "src", "bot.py")

@app.route("/")
def home():
    return "API rodando! Use /start para iniciar o bot."

@app.route("/start")
def start_bot():
    if os.path.exists(BOT_PATH):
        subprocess.Popen(["python", BOT_PATH])
        return f"Bot iniciado a partir de {BOT_PATH}"
    else:
        return "Erro: Arquivo bot.py não encontrado!", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
