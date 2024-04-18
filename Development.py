import pyfiglet
from pyfiglet import Figlet

from land_info import land_info, edit_land_info
from invoice_details import invoice_written, print_invoice_data, edit_invoice_data
from management import return_land, record_customer_details, check_customer_details

while True:
    lands = land_info(r'land.txt')

    print(pyfiglet.figlet_format("Techno Property", justify="center", font="starwars", width=110))
    print("\n\t\t\t\t\tHello Customer!")
    print("\n\t\t\t\t\tWhat would you like to do?")
    print("\n\t\t\t\t1. Print the List of Lands.")
    print("\t\t\t\t2. Print the List of Available Lands.")
    print("\t\t\t\t3. Print the List of Not Available Lands.")
    print("\t\t\t\t4. Rent land.")
    print("\t\t\t\t5. Return land.")

    question_1 = int(input("\n Enter the above given options:  "))

    if question_1 == 1:
        for land in lands:
            print(f"Kitta Number: {land[0]}, City/District: {land[1]}, Direction: {land[2]}, Area(in Anna): {land[3]}, Price(In NPR): {land[4]}, Availability: {land[5]} ")
        
    elif question_1 == 2:
        Available_lands = [land for land in lands if 'Available' in land]
        for land in Available_lands:
            print(f"Kitta Number: {land[0]}, City/District: {land[1]}, Direction: {land[2]}, Area(in Anna): {land[3]}, Price(In NPR): {land[4]}, Availability: {land[5]} ")

    elif question_1 == 3:
        not_available_lands = [land for land in lands if 'Not_Available' in land]
        for land in not_available_lands:
            print(f"Kitta Number: {land[0]}, City/District: {land[1]}, Direction: {land[2]}, Area(in Anna): {land[3]}, Price(In NPR): {land[4]}, Availability: {land[5]} ")

    elif question_1 == 4:
        Available_lands = [land for land in lands if 'Available' in land]
        rent_question_1 = input("\nWhich land would you want to rent? (Enter the Kitta number): ")
        rented_land = [land for land in Available_lands if land[0] == int(rent_question_1)]
        
        if rented_land:
            name = input("\nWhat is your name?: ")
            record_customer_details(r'Customers.txt', name, rent_question_1)
            duration = int(input("\nHow long are you going to rent the land for? (in months): "))
            rented_land = rented_land[0]
            print("\nRent successful")
            invoice_written(name, duration, rented_land[0], rented_land[1], rented_land[2], rented_land[3], rented_land[4])
            edit_land_info(r'Land.txt', rented_land[0])

            Available_lands = [land for land in lands if 'Available' in land]
            
        else:
            print("That land is not available")
        
        rent_question_2 = input("\nWould you like to rent another land? (y/n): ")
        if rent_question_2.lower() == 'y':
            rent_question_3 = input("\nWhich land do you want to rent? (Enter the Kitta number): ")
            rented_land_2 = [land for land in Available_lands if land[0] == int(rent_question_3)]
            if rented_land_2:
                rented_land_2 = rented_land_2[0]
                print("Rent Successfull")
                edit_invoice_data(name,rented_land_2[0],rented_land_2[1],rented_land_2[2],rented_land_2[3],rented_land_2[4])
                edit_land_info(r'Land.txt', rented_land_2[0])
                record_customer_details(r'Customers.txt', name, rent_question_3)
            else:
                print("That land is not available")

        print_invoice_data()

    elif question_1 == 5:
        return_question = input("What is your name?: ")
        return_question_1 = int(input("Enter the Kitta number of the land you want to return: "))
        if check_customer_details(r'Customers.txt', return_question, return_question_1):
            return_land(r'Land.txt', return_question_1)
            print(f"Kitta number {return_question_1} has been returned by {return_question}.")
        else:
            print(f"No rent for Kitta number {return_question_1} has been made by {return_question}.")


        

