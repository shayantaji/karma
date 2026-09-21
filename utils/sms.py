import requests
from django.conf import settings

def send_verify_sms(phone, code):
    try:
        url = "https://rest.payamak-panel.com/api/SendSMS/SendOtp"

        data = {
            "username": settings.MELIPAYAMAK_USERNAME,
            "password": settings.MELIPAYAMAK_API_KEY,
            "to": phone,
            "from": settings.MELIPAYAMAK_SENDER,
            "code": code,
        }

        response = requests.post(url, data=data, timeout=10)

        print(response.text)
        return response.ok

    except Exception as e:
        print(type(e))
        print(e)
        return False