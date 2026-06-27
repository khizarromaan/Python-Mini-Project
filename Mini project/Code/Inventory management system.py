def load():
    items = {}
    try:
        f = open("inventory.txt", "r")
        for line in f:
            d = line.strip().split(",")
            if len(d) == 6:
                items[d[0]] = {
                    "name": d[1],
                    "category": d[2],
                    "price": float(d[3]),
                    "stock": int(d[4]),
                    "reorder": int(d[5])
                }
        f.close()
    except FileNotFoundError:
        pass
    return items

def save(items):
    f = open("inventory.txt", "w")
    for pid in items:
        p = items[pid]
        f.write(pid + "," + p["name"] + "," + p["category"] + "," +
                str(p["price"]) + "," + str(p["stock"]) + "," +
                str(p["reorder"]) + "\n")
    f.close()

def add(items):
    pid = input("Product ID: ")
    if pid in items:
        print("Product already exists.")
        return

    name = input("Product Name: ")
    cat = input("Category: ")

    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        reorder = int(input("Reorder Level: "))
    except ValueError:
        print("Invalid input.")
        return

    items[pid] = {
        "name": name,
        "category": cat,
        "price": price,
        "stock": stock,
        "reorder": reorder
    }

    print("Product Added.")

def stock_in(items):
    pid = input("Product ID: ")

    if pid not in items:
        print("Product not found.")
        return

    try:
        qty = int(input("Quantity: "))
    except ValueError:
        print("Invalid input.")
        return

    items[pid]["stock"] += qty
    print("Stock Updated.")

def stock_out(items):
    pid = input("Product ID: ")

    if pid not in items:
        print("Product not found.")
        return

    try:
        qty = int(input("Quantity: "))
    except ValueError:
        print("Invalid input.")
        return

    if qty > items[pid]["stock"]:
        print("Insufficient Stock.")
    else:
        items[pid]["stock"] -= qty
        print("Stock Updated.")

def report(items):
    if len(items) == 0:
        print("No Products.")
        return

    total = 0
    cats = set()
    low = []

    print("\nInventory Report")
    print("-" * 60)

    for pid in items:
        p = items[pid]
        value = p["price"] * p["stock"]
        total += value
        cats.add(p["category"])

        print("ID:", pid)
        print("Name:", p["name"])
        print("Category:", p["category"])
        print("Price:", p["price"])
        print("Stock:", p["stock"])
        print("Value:", value)
        print()

        if p["stock"] <= p["reorder"]:
            low.append(p["name"])

    print("Total Inventory Value:", total)
    print("Unique Categories:", len(cats))

    print("\nItems Below Reorder Level")
    if len(low) == 0:
        print("None")
    else:
        for i in low:
            print(i)

items = load()

while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. Inventory Report")
    print("5. Save and Exit")

    try:
        ch = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid Input.")
        continue

    if ch == 1:
        add(items)
    elif ch == 2:
        stock_in(items)
    elif ch == 3:
        stock_out(items)
    elif ch == 4:
        report(items)
    elif ch == 5:
        save(items)
        print("Inventory Saved.")
        break
    else:
        print("Invalid Choice.")