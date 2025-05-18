import requests
import json
from config import token, chat_id


def send_poll(token, chat_id, question, options):
    url = f"https://api.telegram.org/bot{token}/sendPoll"
    payload = {
        'chat_id': chat_id,
        'question': question,
        'options': json.dumps(options),
        'is_anonymous': True
    }
    response = requests.post(url, data=payload)
    return response.json()


# Пример использования
question = "Любимый день недели"
options = ["Понедельник",
           "Вторник",
           "Среда",
           "Четверг",
           "Пятница",
           "Суббота",
           "Воскресенье"]

print(send_poll(token, chat_id, question, options))
