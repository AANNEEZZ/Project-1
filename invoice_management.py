import datetime
import uuid

def generate_invoice_id():
    return str(uuid.uuid4())

def invoice_written(name, duration, kitta_number, city, direction, area, price):
    try:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        invoice_id = generate_invoice_id()
        filename = f"Invoice_{invoice_id}.txt"
        total = duration * price
        with open(filename,'w') as file:
            file.write(f"Invoice ID: {invoice_id}\n")
            file.write("FROM:\n")
            file.write(f"\tTechno Property Nepal\n")
            file.write("TO:\n")
            file.write(f"{name}\n")
            file.write(f"Kitta Number: {kitta_number}\n")
            file.write(f"City/District: {city}\n")
            file.write(f"Direction: {direction}\n")
            file.write(f"Area(in Anna): {area}\n")
            file.write(f"Rate(in NPR): {price}\n")
            file.write(f"Duration: {duration} months\n")
            file.write(f"Total: {total}\n")
            file.write(f"Date: {date}\n")
        return filename
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_invoice_data(filename, duration, new_kitta_number, new_city, new_direction, new_area, new_price):
    try:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = new_price * duration
        with open(filename,'a') as file:
            file.write(f"\nKitta Number: {new_kitta_number}\n")
            file.write(f"City/District: {new_city}\n")
            file.write(f"Direction: {new_direction}\n")
            file.write(f"Area(in Anna): {new_area}\n")
            file.write(f"Rate(in NPR): {new_price}\n")
            file.write(f'Duration: {duration} months\n')
            file.write(f"Total: {total}\n")
            file.write(f"Date: {date}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_total(filename):
    try:
        total_amount = 0
        with open(filename, 'r') as file:
            for line in file:
                if "Total:" in line:
                    price = float(line.split(":")[1].strip())
                    total_amount += price
        
        # Append total amount to the invoice file
        with open(filename, 'a') as file:
            file.write(f"\n\n{' '*18}Total Amount = {total_amount}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def return_invoice(name, kitta_number, city_district, direction, area, price):
    try:
        return_invoice_id = generate_invoice_id()
        filename = f"Return_Invoice_{return_invoice_id}.txt"
        with open(filename, 'a') as file:
            file.write(f"Name: {name}\n")
            file.write(f"Kitta Number: {kitta_number}\n")
            file.write(f"City/District: {city_district}\n")
            file.write(f"Direction: {direction}\n")
            file.write(f"Area: {area}\n")
            file.write(f"Rate: {price}\n\n")
    
        return filename
    except Exception as e:
        print(f"An error occurred: {e}")

def return_invoice_with_fine(name, kitta_number, city_district, direction, area, price, fine):
    try:
        return_invoice_with_fine_id = generate_invoice_id()
        filename = f"Return_Invoice_with_fine_{return_invoice_with_fine_id}.txt"
        price = float(price)
        fine = float(fine)
        total_price = float(price + fine)
        with open(filename, 'a') as file:
            file.write(f"Invoice ID: {return_invoice_with_fine_id}\n")
            file.write("FROM:\n")
            file.write(f"\tTechno Property Nepal\n")
            file.write("TO:\n")
            file.write(f"Name: {name}\n")
            file.write(f"Kitta Number: {kitta_number}\n")
            file.write(f"City/District: {city_district}\n")
            file.write(f"Direction: {direction}\n")
            file.write(f"Area: {area}\n")
            file.write(f"Price: {total_price}\n")

    except Exception as e:
        print(f"An error occurred: {e}")
