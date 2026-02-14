import requests

import requests

def get_fear_greed():
    """
    دریافت Fear & Greed Index از alternative.me
    خروجی: عدد بین 0 تا 100
    در صورت خطا، مقدار پیش‌فرض 50 برگردانده می‌شود
    """
    try:
        url = "https://api.alternative.me/fng/"
        response = requests.get(url, timeout=5)
        data = response.json()
        value = int(data['data'][0]['value'])
        return value
    except Exception as e:
        print(f"[Warning] Failed to get Fear & Greed index: {e}")
        return 50

