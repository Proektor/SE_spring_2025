import requests


def get_updates(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    return response.json()


# Пример использования
token = ""
print(get_updates(token))
