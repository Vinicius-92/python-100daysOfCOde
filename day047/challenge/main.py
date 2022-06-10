import smtplib

import requests
from bs4 import BeautifulSoup

MY_EMAIL = "ERASED FOR SECURITY"
MY_PASSWORD = "ERASED FOR SECURITY"
PRICE_I_AM_WILLING_TO_PAY = 140
URL_RICE_COOKER = "https://www.amazon.com.br/Panela-El%C3%A9trica-Oster-CKSTRC4723-017-Vermelho/dp/B0748VSP1S/ref=sr_1_12?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2TBS3LUCH3UB3&keywords=rice+cooker&qid=1654729263&sprefix=rice+coo%2Caps%2C611&sr=8-12&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"

header = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}

response = requests.get(
    url=URL_RICE_COOKER,
    headers=header
)

soup = BeautifulSoup(response.text, 'html.parser')
price_tag = soup.select_one(selector="#attach-base-product-price")
price_today = int(price_tag["value"])

if price_today <= PRICE_I_AM_WILLING_TO_PAY:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Rice cooker price just dropped!\n\nGo by now!.\n\n{URL_RICE_COOKER}"
        )
