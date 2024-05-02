def record_customer_details(filename, name, kitta_number, date, duration):
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                if name == data[0] and int(kitta_number) == int(data[1]):
                    return
        with open(filename, 'a') as file:
            file.write(f"{name}, {kitta_number}, {date}, {duration}\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error recording customer details: {e}")

        
def check_customer_details(filename, name, kitta_number):
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                if name == data[0] and int(data[1]) == kitta_number:
                    return True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error checking customer details: {e}")
    return False

def read_customer_details(filename, name):
    customers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                if data[0] == name:
                    customer = [data[0], int(data[1]), int(data[-1])]
                    customers.append(customer)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading customer details: {e}")
    return customers

def record(filename, name, kitta_number, date, duration):
    try:
        with open(filename, 'a')as file:
            file.write(f"{name}, {kitta_number}, {date}, {duration} months\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")

def count_customer_details(filename, name):
    counter = 0
    try:
        with open(filename,'r') as file:
            for line in file:
                data = line.split(', ')
                if name == data[0]:
                    counter +=1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error counting customer details: {e}")
    return counter 
    
    
