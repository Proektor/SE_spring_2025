import requests


def get_updates(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    return response.json()


# Пример использования
token = "7709538685:AAH3nikbdFya1SUGi16SkWoocf7aFLsnIj8"
print(get_updates(token))
