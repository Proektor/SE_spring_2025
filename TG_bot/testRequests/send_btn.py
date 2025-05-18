import requests
import json
from config import token, chat_id


def send_inline_keyboard(token, chat_id, text, buttons):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    keyboard = {
        'inline_keyboard': [[{'text': btn_text, 'callback_data': btn_data}
                             for btn_text, btn_data in buttons]]
    }
    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': json.dumps(keyboard)
    }
    response = requests.post(url, data=payload)
    return response.json()


# Пример использования
buttons = [("Опция 1", "option1"),
           ("Опция 2", "option2"),
           ("Опция 3", "option3")]
text = "Выбери опцию:"

print(send_inline_keyboard(token, chat_id, text, buttons))
