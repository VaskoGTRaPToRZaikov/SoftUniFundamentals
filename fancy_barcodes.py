import re

number_of_barcodes = int(input())
product_group = ""
pattern = r"^@[#]+([A-Z][A-Za-z0-9]{4,}[A-Z])@[#]+$"

for _ in range(number_of_barcodes):
    barcode = input()

    matches = re.search(pattern, barcode)
    if matches:
        valid_barcode = matches.group(1)
        product_group = ''.join(char for char in valid_barcode if char.isdigit())

        if not product_group:
            product_group = "00"

        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

    product_group = ""