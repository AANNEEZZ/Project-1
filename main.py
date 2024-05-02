'''
Code Written By Anij Gurung
'''

import datetime

from land_management import land_info, rent_land, display_banner, return_land
from invoice_management import invoice_written, edit_invoice_data, return_invoice, calculate_total, return_invoice_with_fine
from record_management import  record_customer_details, check_customer_details, count_customer_details, read_customer_details, record


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
    print("\t\t\t\t6.Refund")
    print("\t\t\t\t0.Exit")

    try:
        question_1 = int(input("\nEnter the above given options: "))
    except ValueError:
        print("Please enter a valid option (0-6).")
        continue

    if question_1 == 1:
        # Print all lands
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*headers))
        print("-" * 90)
        for land in lands:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*land))
            
    elif question_1 == 2:
        available_lands = [land for land in lands if land[-1] == 'Available']
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*headers))
        print("-" * 90)
        for land in available_lands:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*land))

    elif question_1 == 3:
        not_available_lands = [land for land in lands if land[-1] == 'Not_Available']
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*headers))
        print("-" * 90)
        for land in not_available_lands:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*land))
            
    elif question_1 == 4:
        try:
            Available_lands = [land for land in lands if 'Available' in land]
            rent_question_1 = int(input("\nWhich land would you want to rent? (Enter the Kitta number): "))
            if rent_question_1 <= 0:
                raise ValueError("Please enter a positive integer for the Kitta number.")
            
            rented_land = [land for land in Available_lands if land[0] == rent_question_1]
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if rented_land:
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                name = input("\nWhat is your name?: ")
                duration = int(input("\nHow long are you going to rent the land for? (in months): "))
                if duration <= 0:
                    raise ValueError("Please enter a positive integer for the duration.")
                rented_land = rented_land[0]
                record_customer_details(r'Customers.txt', name, rent_question_1, date, duration)
                print("\nrent successful")
                filename = invoice_written(name, duration, rented_land[0], rented_land[1], rented_land[2], rented_land[3], rented_land[4])
                rent_land(r'Land.txt', rented_land[0])
                record(r'record.txt', name, rent_question_1, date, duration)
                Available_lands = [land for land in lands if 'Available' in land]
                while True:
                    Available_lands = [land for land in lands if 'Available' in land]
                    rent_question_2 = input("\nWould you like to rent another land? (y/n): ")
                    if rent_question_2.lower() == 'y':
                        rent_question_3 = int(input("\nWhich land do you want to rent? (Enter the Kitta number): "))
                        if rent_question_3 <= 0:
                            raise ValueError("Please enter a positive integer for the Kitta number.")
                        rented_land_2 = [land for land in Available_lands if land[0] == rent_question_3]
                        if rented_land_2:
                            duration_2 = int(input("\nHow long are you going to rent the land for? (in months): "))
                            if duration_2 <= 0:
                                raise ValueError("Please enter a positive integer for the duration.")
                            rented_land_2 = rented_land_2[0]
                            print("rent Successful")
                            edit_invoice_data(filename, duration_2, rented_land_2[0], rented_land_2[1], rented_land_2[2], rented_land_2[3], rented_land_2[4])
                            rent_land(r'Land.txt', rented_land_2[0])
                            record_customer_details(r'Customers.txt', name, rent_question_3, date, duration_2)
                            record(r'record.txt', name, rent_question_3, date, duration_2)
                        else:
                            print("\nThat land is not available")
                    else:
                        break
            
                calculate_total(filename)
            else:
                print("That land is not available")

        except ValueError as e:
            if "invalid literal for int() " in str(e):
                print("Error: Invalid input. Please enter a valid integer.")
            else:
                print(f"Error: {e}")

    elif question_1 == 5:
        try:
            return_question = input("\nWhat is your name?: ")
            customer_details = read_customer_details(r'Customers.txt', return_question)
            counter = count_customer_details(r'Customers.txt', return_question)
            
            if counter > 0: 
                while True:
                    print(f"\n{return_question} has rented {counter} under their name.")
                    for customer in customer_details:
                        print(f"{customer[1]}")
                    return_question_1 = int(input("\nEnter the Kitta number of the land you want to return: "))
                    if return_question_1 <= 0:
                        raise ValueError("Please enter a positive integer for the Kitta number.")
                    return_duration = int(input("\nHow many months has passed since you rented the land?: "))
                    if return_duration <= 0:
                        raise ValueError("Please enter a positive integer for the duration.")
                    returned_land = [land for land in lands if land[0] == return_question_1][0]
                    if return_duration > int(customer[-1]): 
                        rate_of_Fine = float(0.15 * float(returned_land[-2]))
                        fine = float(rate_of_Fine * (return_duration - float(customer[-1])))
                        print(f"\nYou are fined NPR {rate_of_Fine} for returning the land late.")
                        return_land(r'Land.txt', return_question_1)
                        print(f"\nKitta number {return_question_1} has been returned by {return_question}.")
                        # Generate return invoice
                        return_invoice_with_fine(return_question, returned_land[0], returned_land[1], returned_land[2], returned_land[3], returned_land[4], fine)
                        counter = count_customer_details(r'Customers.txt', return_question) #updating the counter
                        customer_details = read_customer_details(r'Customers.txt', return_question) #updating the customer_details
                        
                    else:    
                        if check_customer_details(r'Customers.txt', return_question, return_question_1):
                            return_land(r'Land.txt', return_question_1)
                            print(f"\nKitta number {return_question_1} has been returned by {return_question}.")
                            # Generate return invoice
                            return_invoice(return_question, returned_land[0], returned_land[1], returned_land[2], returned_land[3], returned_land[4])
                            counter = count_customer_details(r'Customers.txt', return_question) #updating the counter
                            customer_details = read_customer_details(r'Customers.txt', return_question) #updating the customer_details
                        else:
                            print(f"\nNo rent for Kitta number {return_question_1} has been made by {return_question}.")
                        
                    if counter > 0:
                        return_question_2 = input("\nWould you like to return other lands? (y/n): ")
                        if return_question_2.lower() != "y":
                            break
                    
                    else:
                        break
            else:
                print(f"\n{return_question} hasn't rented any land. ")
            
        except ValueError as e:
            if "invalid literal for int() " in str(e):
                print("Error: Invalid input. Please enter a valid integer.")
            else:
                print(f"Error: {e}")

    elif question_1 == 6:
        try:
            refund_question = input("\nWhat is your name?: ")
            customer_details = read_customer_details(r'Customers.txt', refund_question)
            counter = count_customer_details(r'Customers.txt', refund_question) #re-declaring the counter
            lands = land_info(r'Land.txt')
            if counter > 0:
                print(f"\n{refund_question} has rented {counter} under their name.")
                for customer in customer_details:
                    print(f"{customer[1]}")

                refund_land = int(input("\nEnter the kitta number of the land of which you want refund: "))
                if refund_land <= 0:
                    raise ValueError("Please enter a positive integer for the Kitta number.")
                refund_duration = int(input("\nHow long have you rented the land?: "))
                if refund_duration <= 0:
                    raise ValueError("Please enter a positive integer for the duration.")
                rented_months = 0
                total_price = 0

                # Find the rented months for the specified land
                for customer in customer_details:
                    if refund_land == customer[1]:
                        rented_months = customer[-1]
                        break

                # Find the total price for the specified land
                for land in lands:
                    if refund_land == land[0]:
                        total_price = land[-2]
                        break
                
                if refund_duration < rented_months:
                    remaining_months = rented_months - refund_duration
                    refund_rate = remaining_months / rented_months
                    refund_amount = total_price * refund_rate
                    print(f"\nRefund Amount: NPR {refund_amount}")
                    return_land(r'Land.txt', refund_land)    
                else:
                    print("You don't meet the requirement for refund.") 

            
            else:
                print(f"{refund_question} hasn't rented any lands.")
        
        except ValueError as e:
            if "invalid literal for int() " in str(e):
                print("Error: Invalid input. Please enter a valid integer.")
            else:
                print(f"Error: {e}")

    elif question_1 == 0:
        break

    else:
        break