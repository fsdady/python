import requests
import time

def send_message(token, chat_id, text):
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("پیام با موفقیت ارسال شد.")
    else:
        print("مشکلی در ارسال پیام به وجود آمده است.")

# توکن ربات تلگرام خود را در این قسمت وارد کنید
token = "6043246928:AAFAjhgyo8djiaR-erh2RNUnUM7mR7BkP4s"

# شناسه چت کاربر یا گروه را در این قسمت وارد کنید
chat_id = "5411173999"

# متن پیام را در این قسمت وارد کنید
text = "سلام! این یک پیام تستی است."

send_message(token, chat_id, text)

