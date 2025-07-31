import requests
from bs4 import BeautifulSoup


url = "https://www.amazon.com.au/Shrek-Costume-Halloween-Cosplay-Green/dp/B07DFD315M/ref=sr_1_3?dib=eyJ2IjoiMSJ9.sbh5oYLRAVP2BbLlwQr44lnH3eV18mvfw5Lige7dC5nGlD-Q8usO1TYKqTWOHyopLJSUUmMBsdHd45rJq5aGueLo37F6goASZuVacBqpzMliiyRkxoHR-JqtDwXO_rKLU0ogeeB5KkBMltipnC69c3PHOLO3iRquakhT7CN4E_6No6e3gTqklLmTsjZtuBvhYFd_BORfCq0eUaqCt5Ch7_Bg9O_wsltGZPgQ9L3vDzz6HvhhKzG8TfVRQjjj2BUqYzE3cmNeBhqLY-APTYP-77VoV48CJkXlqq-cm05IYgk.BS-Uejru4BVMeJgGqJjU5NM87SumCs91KeqqlxurLPo&dib_tag=se&keywords=shrek+mask&qid=1753153352&sr=8-3"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

price_element = soup.find("span", {"class": "a-offscreen"})
if price_element:
    price = price_element.text.strip()
    print(f"Price: {price}")
else:
    print("Price element not found on the page.")