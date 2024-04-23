def land_info(filename):
    Lands = []
    with open(filename,'r') as file:
        for line in file:
            data = line.strip().replace(',','').split()
            if len(data) >= 6:
                land = [int(data[0]), data[1], data[2], int(data[3]), int(data[4]), data[5]]
                Lands.append(land)
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

def edit_land_info(filename, kitta_number):
    updated_lands = []
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

    return updated_lands

def record(filename, name, kitta_number, date, duration):
    with open (filename, 'a')as file:
        file.write(f"{name}, {kitta_number}, {date}, {duration} months\n")