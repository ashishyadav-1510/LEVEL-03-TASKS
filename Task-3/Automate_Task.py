import csv
import os
from datetime import datetime
from collections import defaultdict

# === Auto-create sales_data.csv if not present ===
def generate_sample_csv(filename='sales_data.csv'):
    """
    Creates a sample sales CSV file automatically if it doesn't exist.
    """
    if os.path.exists(filename):
        print(f"[INFO] File '{filename}' already exists.")
        return

    sample_data = [
        ['Date', 'Product', 'Category', 'Quantity', 'Unit_Price'],
        ['2025-07-15', 'Laptop', 'Electronics', '3', '45000'],
        ['2025-07-15', 'Pen', 'Stationery', '50', '10'],
        ['2025-07-16', 'Chair', 'Furniture', '5', '1500'],
        ['2025-07-17', 'Notebook', 'Stationery', '30', '25'],
        ['2025-07-17', 'Smartphone', 'Electronics', '2', '20000']
    ]

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(sample_data)
        print(f"[SUCCESS] Created sample CSV: {filename}")
    except Exception as e:
        print(f"[ERROR] Could not create CSV: {e}")

# === Process CSV and Create Report ===
def read_csv_and_generate_report(input_file='sales_data.csv', report_file='sales_report.txt'):
    """
    Processes the CSV file and generates a formatted text report.
    """
    if not os.path.exists(input_file):
        print(f"[ERROR] Input file '{input_file}' not found.")
        return

    total_sales = 0
    category_sales = defaultdict(float)
    records = []

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    qty = int(row['Quantity'])
                    price = float(row['Unit_Price'])
                    sale = qty * price
                    category = row['Category']
                    total_sales += sale
                    category_sales[category] += sale
                    records.append({
                        'Date': row['Date'],
                        'Product': row['Product'],
                        'Category': category,
                        'Quantity': qty,
                        'Unit_Price': price,
                        'Sale': sale
                    })
                except (ValueError, KeyError) as e:
                    print(f"[WARNING] Skipping row due to error: {e}")

    except Exception as e:
        print(f"[ERROR] Reading CSV failed: {e}")
        return

    # === Write formatted report with UTF-8 ===
    try:
        with open(report_file, 'w', encoding='utf-8') as report:
            report.write("======= AUTOMATED SALES REPORT =======\n")
            report.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            report.write(f"{'Date':<12}{'Product':<15}{'Category':<15}{'Qty':<5}{'Price':<10}{'Sale':<10}\n")
            report.write("-" * 70 + "\n")

            for r in records:
                report.write(f"{r['Date']:<12}{r['Product']:<15}{r['Category']:<15}"
                             f"{r['Quantity']:<5}{r['Unit_Price']:<10.2f}{r['Sale']:<10.2f}\n")

            report.write("\n[SUMMARY]\n")
            report.write(f"Total Sales: ₹{total_sales:.2f}\n")
            report.write("Sales by Category:\n")
            for cat, amount in category_sales.items():
                report.write(f"  - {cat}: ₹{amount:.2f}\n")
            report.write("======================================\n")

        print(f"[SUCCESS] Report created: {report_file}")

    except Exception as e:
        print(f"[ERROR] Could not write report: {e}")

# === Main Automation Driver ===
def main():
    print("Automating Sales Report Generation\n")
    generate_sample_csv()  # auto-create file
    read_csv_and_generate_report()  # read + report

# === Entry Point ===
if __name__ == "__main__":
    main()
