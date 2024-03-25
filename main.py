import requests
import time

def execute_request():
    try:
        cookies = {
            'googtrans': '/en/ar',
            'reg': '1',
            'googtrans': '/en/ar',
            'show_nt1': '1',
            'Hm_lvt_2b147ccaeef7e49f5f9553cadfdf8428': '1710625627,1710767583,1710846640,1711372064',
            'login': '1',
            'user': '408797432164-156.221.167.231',
            'Hm_lpvt_2b147ccaeef7e49f5f9553cadfdf8428': '1711373435',
        }

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # 'cookie': 'googtrans=/en/ar; reg=1; googtrans=/en/ar; show_nt1=1; Hm_lvt_2b147ccaeef7e49f5f9553cadfdf8428=1710625627,1710767583,1710846640,1711372064; login=1; user=408797432164-156.221.167.231; Hm_lpvt_2b147ccaeef7e49f5f9553cadfdf8428=1711373435',
            'origin': 'https://faucetearner.org',
            'referer': 'https://faucetearner.org/faucet.php',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'act': 'faucet',
        }

        json_data = {}

        response = requests.post('https://faucetearner.org/api.php', params=params, cookies=cookies, headers=headers, json=json_data)
        print(response.json())
        return response.text
    except Exception as e:
        print("An error occurred:", e)
        return ""

def check_for_congratulations(response_text):
    if "Congratulations" in response_text:
        # إذا كان الرد يحتوي على "Congratulations"
        # إضافة نص إلى الرسالة توضح أنه تم من الحساب الثاني
        response_text_with_note = f"{response_text} (تم من الحساب الثاني)"
        send_telegram_message(response_text_with_note)

def send_telegram_message(message):
    token = '6765046025:AAEwX_oVI8nhQCjZ0H60p7AXz_vpn0KLNUA'
    chat_id = '831625834'
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, json=payload)

while True:
    response_text = execute_request()
    check_for_congratulations(response_text)
    time.sleep(60)
