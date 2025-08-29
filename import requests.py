import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time   

# Amazon product URL
url = "https://www.amazon.com.au/Quilton-Toilet-Tissue-Sheets-11x10cm/dp/B09T1F745V/ref=sr_1_3?crid=135JD7B33NAWV"

# Simple headers to look like a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

while True:  # loop forever
    print("Getting page...")

    # Get the webpage
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Save the HTML so you can look at it
    with open("page.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Page saved to page.html")

    # Look for price
    price = None

    # First try Amazon’s known price selectors
    selectors = [
        "#priceblock_ourprice",
        "#priceblock_dealprice",
        "#priceblock_saleprice",
        ".a-price .a-offscreen"
    ]
    for selector in selectors:
        price_tag = soup.select_one(selector)
        if price_tag:
            price = price_tag.get_text(strip=True)
            print(f"Selected price from selector {selector}: {price}")
            break

    # Fallback: your original $ line scanning
    if not price:
        print("Showing all text with $ symbol:")
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

        # Try to pick the most likely price (first short line with $)
        for line in dollar_lines:
            if len(line) < 15 and any(char.isdigit() for char in line):
                price = line
                print(f"Selected price: {price}")
                break

    # Save to CSV - APPEND mode to keep history
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Check if CSV already has data
        with open("price.csv", "r", encoding="utf-8") as f:
            existing_data = f.read()
            file_exists = len(existing_data.strip()) > 0
    except FileNotFoundError:
        file_exists = False

    with open("price.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Timestamp", "Price", "Status"])
            print("Created new CSV file with headers")

        if price:
            writer.writerow([timestamp, price, "Found"])
            print(f"Success! Price added: {price}")
        else:
            writer.writerow([timestamp, "Not found", "Failed"])
            print("No price found - logged to CSV")

    print("Data appended to price.csv")
    print("Check page.html in your browser to see what Amazon sent")

    print("Getting the next price...")
    time.sleep(60)
