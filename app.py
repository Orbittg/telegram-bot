from flask import Flask, request
from telegram import Bot

app = Flask(__name__)
bot = Bot(token="AAHGha80jDa9EA8km5QlaKiCV937QmFJnr8")

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    if update:
        bot.send_message(chat_id=update["message"]["chat"]["id"], text="Привет!")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
