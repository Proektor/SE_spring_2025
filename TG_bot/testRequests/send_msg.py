import requests
from config import token, chat_id


def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, data=payload)
    return response.json()


# Пример использования
text = "Проверка"
print(send_message(token, chat_id, text))
