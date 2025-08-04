import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://www.amazon.com.au/Shrek-Costume-Halloween-Cosplay-Green/dp/B07DFD315M"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

# write soup to file
with open("soup.html", "w", encoding="utf-8") as file:
    file.write(str(soup))
    
price_element = soup.find("span", {"class": "a-offscreen"})
if price_element:
    price = price_element.text.strip()
    print(f"Price: {price}")
else:
    print("Price element not found on the page.")

# Save to CSV
with open("seller_prices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Seller", "Price"])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #writer.writerow([timestamp, "Main Product", main_price])

    if offers:
        for idx, offer in enumerate(offers, start=1):
            price = offer.text.strip()
            writer.writerow([timestamp, f"Seller {idx}", price])
    else:
        writer.writerow([timestamp, "Other Sellers", "None found"])

print("Data saved to seller_prices.csv!")


