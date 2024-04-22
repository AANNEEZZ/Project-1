def return_land(filename, kitta_number):
    updated_lands = []
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
            rented_kitta_number = int(customer.strip().split(',')[0])
            if rented_kitta_number == kitta_number:
                continue  # Skip the line for the returned land
            file.write(customer)


def record_customer_details(filename, name, kitta_number):
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(', ')
            if name == data[0] and int(kitta_number) == int(data[1]):
                return

    with open(filename, 'a') as file:
        file.write(f"{name}, {kitta_number}\n")


def check_customer_details(filename, name, kitta_number):
    with open(filename, 'r') as file:
        for line in file:
            data = line.split(', ')
            if name == data[0] and int(data[1]) == kitta_number:
                return True
    return False

def count_customer_details(filename, name):
    counter = 0
    with open(filename,'r')as file:
        for line in file:
            data = line.split(', ')
            if name == data[0]:
                counter +=1
        
        return counter

