import datetime

from land_info import land_info, edit_land_info, display_banner, record
from invoice_details import invoice_written, print_invoice_data, edit_invoice_data, return_invoice, calculate_total
from management import return_land, record_customer_details, check_customer_details,count_customer_details, read_customer_details


display_banner()
print("\n\t\t\t\t\tHello Customer!")

while True:
    lands = land_info(r'Land.txt')
    headers = ["Kitta Number", "City/District", "Direction", "Area(in Anna)", "Price(In NPR)", "Availability"]

    print("\n\t\t\t\t\tWhat would you like to do?")
    print("\n\t\t\t\t1.Print the List of Lands.")
    print("\t\t\t\t2.Print the List of Available Lands.")
    print("\t\t\t\t3.Print the List of Not Available Lands.")
    print("\t\t\t\t4.Rent land.")
    print("\t\t\t\t5.Return land.")

    question_1 = int(input("\nEnter the above given options:  "))

    if question_1 == 1:
        # Print all lands
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*headers))
        print("-" * 90)
        for land in lands:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*land))
            
    elif question_1 == 2:
        Available_lands = [land for land in lands if 'Available' in land]
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*headers))
        print("-" * 90)
        for land in Available_lands:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*land))    

    elif question_1 == 3:
        not_available_lands = [land for land in lands if 'Not_Available' in land]
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*headers))
        print("-" * 90)
        for land in not_available_lands:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*land))

    elif question_1 == 4:
        Available_lands = [land for land in lands if 'Available' in land]
        rent_question_1 = input("\nWhich land would you want to rent? (Enter the Kitta number): ")
        rented_land = [land for land in Available_lands if land[0] == int(rent_question_1)]
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if rented_land:
            name = input("\nWhat is your name?: ")
            record_customer_details(r'Customers.txt', name, rent_question_1)
            duration = int(input("\nHow long are you going to rent the land for? (in months): "))
            rented_land = rented_land[0]
            print("\nRent successful")
            invoice_written(name, duration, rented_land[0], rented_land[1], rented_land[2], rented_land[3], rented_land[4])
            edit_land_info(r'Land.txt', rented_land[0])
            record(r'record.txt', name, rent_question_1, date, duration)
            Available_lands = [land for land in lands if 'Available' in land]
            while True:
                Available_lands = [land for land in lands if 'Available' in land]
                rent_question_2 = input("\nWould you like to rent another land? (y/n): ")
                if rent_question_2.lower() == 'y':
                    rent_question_3 = input("\nWhich land do you want to rent? (Enter the Kitta number): ")
                    rented_land_2 = [land for land in Available_lands if land[0] == int(rent_question_3)]
                    if rented_land_2:
                        duration_2 = int(input("\nHow long are you going to rent the land for? (in months): "))
                        rented_land_2 = rented_land_2[0]
                        print("Rent Successful")
                        edit_invoice_data(duration_2, rented_land_2[0], rented_land_2[1], rented_land_2[2], rented_land_2[3], rented_land_2[4])
                        edit_land_info(r'Land.txt', rented_land_2[0])
                        record_customer_details(r'Customers.txt', name, rent_question_3)
                        record(r'record.txt', name, rent_question_3, date, duration_2)
                    else:
                        print("That land is not available")
                else:
                    break
        
            calculate_total()
            print_invoice_data()
        else:
            print("That land is not available")


    elif question_1 == 5:
        return_question = input("\nWhat is your name?: ")
        customer_details = read_customer_details(r'Customers.txt', return_question)
        match = [customer for customer in customer_details if customer[0] == return_question]
        counter = count_customer_details(r'Customers.txt', return_question)
        if counter > 0: 
            while True:
                print(f"\n{return_question} has rented {counter} under their name.")
                for customer in customer_details:
                    print(f"{customer[1]}")
                return_question_1 = int(input("\nEnter the Kitta number of the land you want to return: "))
                if check_customer_details(r'Customers.txt', return_question, return_question_1):
                    return_land(r'Land.txt', return_question_1)
                    print(f"Kitta number {return_question_1} has been returned by {return_question}.")
                    # Generate return invoice
                    returned_land = [land for land in lands if land[0] == return_question_1][0]
                    return_invoice(return_question, returned_land[0], returned_land[1], returned_land[2], returned_land[3], returned_land[4])
                else:
                    print(f"No rent for Kitta number {return_question_1} has been made by {return_question}.")
                
                if count_customer_details(r'Customers.txt', return_question) > 0:
                    return_question_2 = input("Would you like to return other lands? (y/n): ")
                    if return_question_2.lower() != "y":
                        break

                else:
                    break    
            


        

