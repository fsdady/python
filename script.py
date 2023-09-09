#pylint:disable=E0001
import requests
import time

while True:
    response = requests.get('https://api.telegram.org/bot6043246928:AAFAjhgyo8djiaR-erh2RNUnUM7mR7BkP4s/sendMessage?chat_id=5411173999&text=Hiii')
    print(response.text)
    time.sleep(10)
