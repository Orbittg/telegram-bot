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
import logging
from flask import Flask, request
import telepot

app = Flask(__name__)
bot = telepot.Bot('ТВОЙ_ТОКЕН')

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Получаем данные из POST-запроса
        data = request.get_json()
        logging.debug(f"Received data: {data}")  # Логируем входящие данные

        # Извлекаем chat_id и сообщение
        chat_id = data['message']['chat']['id']
        text = "Your message was received!"
        
        # Отправляем ответ в Telegram
        bot.sendMessage(chat_id, text)

        logging.debug("Message sent successfully")  # Логируем успешную отправку

        return '', 200  # Возвращаем статус 200 (OK)
    
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return '', 500  # Возвращаем статус 500 (Ошибка сервера)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
