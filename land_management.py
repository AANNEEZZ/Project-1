def land_info(filename):
    Lands = []
    try:
        with open(filename,'r') as file:
            for line in file:
                data = line.strip().replace(',','').split()
                if len(data) >= 6:
                    land = [int(data[0]), data[1], data[2], int(data[3]), int(data[4]), data[5]]
                    Lands.append(land)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
    return Lands

def display_banner():
    banner = r'''
        
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

        '''

    print(banner)

def rent_land(filename, kitta_number):
    updated_lands = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().replace(',', '').split()
                if len(data) >= 6:
                    if int(data[0]) == kitta_number and data[5] == 'Available':
                        data[5] = 'Not_Available'
                    updated_lands.append(', '.join(data))

        with open(filename, 'w') as file:
            for land in updated_lands:
                file.write('\t' + land + '\n')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error updating file '{filename}': {e}")
    return updated_lands

def return_land(filename, kitta_number):
    updated_lands = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) >= 6:
                    if int(data[0]) == kitta_number and data[5].strip() == 'Not_Available':
                        data[5] = 'Available'
                    updated_lands.append(', '.join(data))
        with open(filename, 'w') as file:
            for land in updated_lands:
                file.write(land + '\n')

        # Update customer's record
        customers_file = 'Customers.txt'
        with open(customers_file, 'r') as file:
            customers = file.readlines()
        with open(customers_file, 'w') as file:
            for customer in customers:
                rented_kitta_number = int(customer.strip().split(',')[1])
                if rented_kitta_number != kitta_number:
                    file.write(customer)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error updating land record: {e}")

