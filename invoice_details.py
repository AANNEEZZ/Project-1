import datetime

def invoice_written(name, duration, kitta_number, city, direction, area, price):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('Invoice.txt','w') as file:
        file.write("FROM:\n")
        file.write(r'''
        
 /$$$$$$$$                  /$$                                 /$$$$$$$                                                     /$$              
|__  $$__/                 | $$                                | $$__  $$                                                   | $$              
   | $$  /$$$$$$   /$$$$$$$| $$$$$$$  /$$$$$$$   /$$$$$$       | $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$   /$$
   | $$ /$$__  $$ /$$_____/| $$__  $$| $$__  $$ /$$__  $$      | $$$$$$$//$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/  | $$  | $$
   | $$| $$$$$$$$| $$      | $$  \ $$| $$  \ $$| $$  \ $$      | $$____/| $$  \__/| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/  | $$    | $$  | $$
   | $$| $$_____/| $$      | $$  | $$| $$  | $$| $$  | $$      | $$     | $$      | $$  | $$| $$  | $$| $$_____/| $$        | $$ /$$| $$  | $$
   | $$|  $$$$$$$|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$/      | $$     | $$      |  $$$$$$/| $$$$$$$/|  $$$$$$$| $$        |  $$$$/|  $$$$$$$
   |__/ \_______/ \_______/|__/  |__/|__/  |__/ \______/       |__/     |__/       \______/ | $$____/  \_______/|__/         \___/   \____  $$
                                                                                            | $$                                     /$$  | $$
                                                                                            | $$                                    |  $$$$$$/
                                                                                            |__/                                     \______/ 

        ''')
        file.write("TO:\n")
        file.write(f"{name}\n")
        file.write(f"Kitta Number: {kitta_number}\n")
        file.write(f"City/District: {city}\n")
        file.write(f"Direction: {direction}\n")
        file.write(f"Area(in Anna): {area}\n")
        file.write(f"Price(in NPR): {price}\n")
        file.write(f"Duration: {duration} months\n")
        file.write(f"Date: {date}\n")

def edit_invoice_data(duration, new_kitta_number, new_city, new_direction, new_area, new_price):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('Invoice.txt','a') as file:

        file.write(f"\nKitta Number: {new_kitta_number}\n")
        file.write(f"City/District: {new_city}\n")
        file.write(f"Direction: {new_direction}\n")
        file.write(f"Area(in Anna): {new_area}\n")
        file.write(f"Price(in NPR): {new_price}\n")
        file.write(f'Duration: {duration} months\n')
        file.write(f"Date: {date}\n")

def calculate_total():
    total_amount = 0
    with open(r'Invoice.txt', 'r') as file:
        for line in file:
            if "Price(in NPR):" in line:
                price = float(line.split(":")[1].strip())
                total_amount += price
    
    # Append total amount to the invoice file
    with open('Invoice.txt', 'a') as file:
        file.write(f"\n\n{' '*18}Total Amount = {total_amount}\n")

def print_invoice_data():
    with open('Invoice.txt', 'r') as file:
        invoice_data = file.read()
        print(invoice_data)        

def return_invoice_blank():
    with open(r'return invoice.txt', 'w')as file:
        file.write("")

def return_invoice(name, kitta_number, city_district, direction, area, price):
    with open(r'return invoice.txt', 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Kitta Number: {kitta_number}\n")
        file.write(f"City/District: {city_district}\n")
        file.write(f"Direction: {direction}\n")
        file.write(f"Area: {area}\n")
        file.write(f"Price: {price}\n\n")

def return_invoice_with_fine(name, kitta_number, city_district, direction, area, price, fine):
    price = int(price)
    fine = int(fine)
    with open(r'return invoice.txt', 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Kitta Number: {kitta_number}\n")
        file.write(f"City/District: {city_district}\n")
        file.write(f"Direction: {direction}\n")
        file.write(f"Area: {area}\n")
        file.write(f"Price: {price} + {fine}\n")

def calculate_invoice_total():
    total = 0
    with open(r'return invoice.txt', 'r') as file:
        for line in file:
            if "Price(in NPR):" in line:
                price = float(line.split(":")[1].strip())
                total += price
    
    # Append total amount to the invoice file
    with open(r'return invoice.txt', 'a') as file:
        file.write(f"\n\n{' '*18}Total Amount = {total}\n")