import csv
from datetime import datetime

# Path to your CSV file
filename = "price.csv"

# Lists to store dates and prices
price_data = []

# Read the CSV file
with open(filename, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            # Parse date and price
            date = datetime.strptime(row['date'], "%Y-%m-%d")
            price = float(row['price'])
            price_data.append((date, price))
        except Exception as e:
            print(f"Skipping row due to error: {e}")

# Ensure there is data
if not price_data:
    print("No valid data found.")
else:
    # Sort data by date
    price_data.sort(key=lambda x: x[0])

    # Calculate average price
    prices = [price for _, price in price_data]
    average_price = sum(prices) / len(prices)

    # Get the latest price
    latest_date, latest_price = price_data[-1]

    # Output results
    print(f"Average Price: ${average_price:.2f}")
    print(f"Latest Price (on {latest_date.date()}): ${latest_price:.2f}")
