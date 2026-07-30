from kavenegar import KavenegarAPI
from django.conf import settings


def send_verify_sms(phone, code):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_API_KEY)

        params = {
            "receptor": phone,
            "message": f"کد تایید شما: {code}"
        }

        response = api.sms_send(params)

        return True

    except Exception as e:

        print("Kavenegar Error:", e)

        return False