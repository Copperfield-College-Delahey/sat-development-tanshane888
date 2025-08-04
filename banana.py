import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Amazon product URL
url = "https://www.amazon.com.au/Shrek-Costume-Halloween-Cosplay-Green/dp/B07DFD315M"

# Simple headers to look like a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Getting page...")

# Get the webpage
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Save the HTML so you can look at it
with open("page.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Page saved to page.html")

# Look for price - try the most common way first
price = None

# Method 3: Manual search - print some elements with $ so you can see what's there
if not price:
    print("Method 2 failed, showing all text with $ symbol:")
    all_text = soup.get_text()
    lines = all_text.split('\n')
    
    dollar_lines = []
    for line in lines:
        line = line.strip()
        if '$' in line and line:
            dollar_lines.append(line)
    
    print(f"Found {len(dollar_lines)} lines with $ symbol:")
    for i, line in enumerate(dollar_lines[:10]):  # Show first 10
        print(f"{i+1}. {line}")

# Save to CSV
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("price.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Price", "Status"])
    
    if price:
        writer.writerow([timestamp, price, "Found"])
        print(f"✅ Success! Price saved: {price}")
    else:
        writer.writerow([timestamp, "Not found", "Failed"])
        print(" No price found")

print("Data saved to price.csv")
print("Check page.html in your browser to see what Amazon sent")