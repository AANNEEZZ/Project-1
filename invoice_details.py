import datetime
import pyfiglet
from pyfiglet import Figlet

def invoice_written(name, duration, kitta_number, city, direction, area, price):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('Invoice.txt','w') as file:
        file.write("FROM:\n")
        file.write(pyfiglet.figlet_format("Techno Property", justify="center", font="avatar", width=110))
        file.write("TO:\n")
        file.write(f"{name}\n")
        file.write(f"Kitta Number: {kitta_number}\n")
        file.write(f"City/District: {city}\n")
        file.write(f"Direction: {direction}\n")
        file.write(f"Area(in Anna): {area}\n")
        file.write(f"Price(in NPR): {price}\n")
        file.write(f"Duration: {duration} months\n")
        file.write(f"Date: {date}\n")

def print_invoice_data():
    with open('Invoice.txt', 'r') as file:
        invoice_data = file.read()
        print(invoice_data)

def edit_invoice_data(duration, new_kitta_number, new_city, new_direction, new_area, new_price):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('Invoice.txt','a') as file:

        file.write(f"\nKitta Number: {new_kitta_number}\n")
        file.write(f"City/District: {new_city}\n")
        file.write(f"Direction: {new_direction}\n")
        file.write(f"Area(in Anna): {new_area}\n")
        file.write(f"Price(in NPR): {new_price}\n")
        file.write(f'Duration: {duration} months')
        file.write(f"Date: {date}\n")

def return_invoice(name, kitta_number):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('return invoice.txt', 'w') as file:
        file.write("FROM:\n")
        file.write(pyfiglet.figlet_format("Techno Property", justify="center", font="avatar", width=110))
        file.write("TO:\n")
        file.write(f"{name}\n")
        file.write(f"Kitta Number: {kitta_number}\n")