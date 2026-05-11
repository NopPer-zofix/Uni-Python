import csv
import Product as prod

CSV_PATH = "D:\\snake\\Uni\\Lab6\\All_Products.csv"
products = []


def load_products():
    """Load products from CSV and return a list of Product objects."""
    loaded = []
    with open(CSV_PATH, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ptype = row['Product_Type'].strip().lower()
            serial = int(row['SerialNumber'])
            title = row['Title'].strip()
            price = float(row['regularPrice']) if row['regularPrice'] else 0.0
            discount = float(row['Discount']) if row['Discount'] else 0.0

            if ptype == 'tv':
                size = int(row['Size']) if row['Size'] else 0
                smart = row['SmartTv'].strip().upper() == 'TRUE' if row['SmartTv'] else False
                manufacturer = row['Manufacturer/Author'].strip()
                obj = prod.TVs(serial, title, price, manufacturer, size, smart, discount)

            elif ptype == 'electronics':
                manufacturer = row['Manufacturer/Author'].strip()
                obj = prod.Electronics(serial, title, price, manufacturer, discount)

            elif ptype == 'book':
                author = row['Manufacturer/Author'].strip()
                year = int(row['Year Published']) if row['Year Published'] else 0
                obj = prod.Books(serial, title, price, author, year, discount)

            else:
                obj = prod.Product(serial, title, price)

            loaded.append(obj)
    return loaded


def list_all(products):
    if not products:
        print("No products loaded.")
        return
    for p in products:
        print(p)


def list_electronics(products):
    filtered = [p for p in products if isinstance(p, prod.Electronics)]
    if not filtered:
        print("No electronic products found.")
        return
    for p in filtered:
        print(p)


def list_non_electronics(products):
    filtered = [p for p in products if not isinstance(p, prod.Electronics)]
    if not filtered:
        print("No non-electronic products found.")
        return
    for p in filtered:
        print(p)


def add_electronic(products):
    print("\n-- Add Electronic Product --")
    serial = int(input("Serial Number: "))
    title = input("Title: ")
    price = float(input("Regular Price: "))
    manufacturer = input("Manufacturer: ")
    discount = float(input("Discount (e.g. 0.1 for 10%): "))
    obj = prod.Electronics(serial, title, price, manufacturer, discount)
    products.append(obj)
    print(f"Added: {obj}")


def add_tv(products):
    print("\n-- Add TV Product --")
    serial = int(input("Serial Number: "))
    title = input("Title: ")
    price = float(input("Regular Price: "))
    manufacturer = input("Manufacturer: ")
    size = int(input("Size (inches): "))
    smart = input("Smart TV? (yes/no): ").strip().lower() == 'yes'
    discount = float(input("Discount (e.g. 0.1 for 10%): "))
    obj = prod.TVs(serial, title, price, manufacturer, size, smart, discount)
    products.append(obj)
    print(f"Added: {obj}")


def add_book(products):
    print("\n-- Add Book --")
    serial = int(input("Serial Number: "))
    title = input("Title: ")
    price = float(input("Regular Price: "))
    author = input("Author: ")
    year = int(input("Year Published: "))
    discount = float(input("Discount (e.g. 0.1 for 10%): "))
    obj = prod.Books(serial, title, price, author, year, discount)
    products.append(obj)
    print(f"Added: {obj}")


def edit_product(products):
    if not products:
        print("No products loaded.")
        return
    serial = int(input("Enter Serial Number of product to edit: "))
    matches = [p for p in products if p.getSerialNumber() == serial]
    if not matches:
        print("Product not found.")
        return
    p = matches[0]
    print(f"Editing: {p}")
    print("What would you like to edit?")
    print("  1) Title")
    print("  2) Regular Price")
    choice = input("Select field: ").strip()
    if choice == '1':
        p.setTitle(input("New Title: "))
    elif choice == '2':
        p.setRegularPrice(float(input("New Price: ")))
    else:
        print("Invalid choice.")
        return
    print(f"Updated: {p}")


def save_products(products):
    with open(CSV_PATH, 'w', newline='', encoding='utf-8-sig') as f:
        fieldnames = ['SerialNumber', 'Product_Type', 'Title',
                      'Manufacturer/Author', 'Year Published',
                      'regularPrice', 'Discount', 'Size', 'SmartTv']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in products:
            row = {
                'SerialNumber': p.getSerialNumber(),
                'Title': p.getTitle(),
                'regularPrice': p.getRegularPrice(),
                'Product_Type': '',
                'Manufacturer/Author': '',
                'Year Published': '',
                'Discount': '',
                'Size': '',
                'SmartTv': ''
            }
            if isinstance(p, prod.TVs):
                row['Product_Type'] = 'TV'
                row['Manufacturer/Author'] = p.getManufacturer()
                row['Discount'] = p.getDiscount()
                row['Size'] = p.getSize()
                row['SmartTv'] = p.getSmartTv()
            elif isinstance(p, prod.Electronics):
                row['Product_Type'] = 'Electronics'
                row['Manufacturer/Author'] = p.getManufacturer()
                row['Discount'] = p.getDiscount()
            elif isinstance(p, prod.Books):
                row['Product_Type'] = 'Book'
                row['Manufacturer/Author'] = p.getAuthor()
                row['Year Published'] = p.getYear()
                row['Discount'] = p.getDiscount()
            else:
                row['Product_Type'] = 'Other'
            writer.writerow(row)
    print(f"Products saved to {CSV_PATH}")


def print_menu():
    print("\n========== Product Manager ==========")
    print("a) Load product data from CSV")
    print("b) List ALL products")
    print("c) List Electronic products")
    print("d) List non-Electronic products")
    print("e) Add Electronic product")
    print("f) Add a TV product")
    print("g) Add a Book")
    print("h) Edit product")
    print("i) Store product data in CSV")
    print("q) Quit")
    print("=====================================")


# ---------- Main Loop ----------
while True:
    print_menu()
    choice = input("Select an option: ").strip().lower()

    match choice:
        case "a":
            products = load_products()
            print(f"{len(products)} products were loaded.")
        case "b":
            list_all(products)
        case "c":
            list_electronics(products)
        case "d":
            list_non_electronics(products)
        case "e":
            add_electronic(products)
        case "f":
            add_tv(products)
        case "g":
            add_book(products)
        case "h":
            edit_product(products)
        case "i":
            save_products(products)
        case "q":
            print("Goodbye!")
            break
        case _:
            print("Option not found. Please try again.")