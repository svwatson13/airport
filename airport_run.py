from airport_classes import *
passengers = []

import time

while True:
    a = 0
    user_input = input('\nDo you wish to: \n1) Create a passenger \n2) Create a plane \n3) Make a flight \n4) List flights '
                       '\n5) Exit \nPlease choose a number: ')
    if user_input == '1':
        passengername = input('\nName of passenger ')
        passengernum = input('Passport Number of passenger ')
        if passengername == "" or passengernum == "":
            print('Error, you failed to enter a key piece of information')
            continue
        else:
            passengername = Passengers(passengername, passengernum)
            print(passengername.name, passengername.passnum)
    elif user_input == '2':
        while True:
            plane = input('\nName of plane ')
            planenum = input('Plane Number ')
            if plane == "" or planenum == "":
                print('Error, you failed to enter a key piece of information')
                continue
            else:
                plane = Planes(plane, planenum)
                print(plane.name, plane.planenum)
                break
    elif user_input == '3':
        flight = input('\nWhats your flight? ')
        while True:
            if a == 1:
                break
            info = input(f'\nDo you want to add info to flight {flight}? (y/n) ')
            if info == 'y':
                origin = input('What is the origin? ')
                destination = input('Where is it going? ')
                planenum = input('What is the plane number ')
                user_input = Flight(origin, destination, planenum)
                while True:
                    exit = input('Do you wish to add passengers? (y/n) ')
                    if exit == 'y':
                        while True:
                            user_input = input('Name of passenger to add (or type exit to quit): ')
                            if user_input == 'exit':
                                print(passengers)
                                break
                            else:
                                passengers.append(user_input)
                    elif exit == 'n':
                        print('\nThank you for adding a flight')
                        a = 1
                        break
                    else:
                        print('Invalid response')
                        a = 1

            elif info == 'n':
                user_input = Flight(flight)
                print('\nThank you for adding a flight')
                b = 1
                break
            else:
                print('Invalid response')
                continue
    elif user_input == '4':
        for i in Flight.class_variable:
            print(i.name)
    elif user_input == '5':
        break
    else:
        print('You didnt register a valid response')
        continue





