from airport_classes import *
passengers = []


while True:
    user_input = input('Do you wish to create a passenger (1), plane (2), flight (3) or exit (4) ')
    if user_input == '1':
        passengername = input('Name of passenger ')
        passengernum = input('Passport Number of passenger ')
        if passengername == "" or passengernum == "":
            print('Error, you failed to enter a key piece of information')
            continue
        else:
            passengername = Passengers(passengername, passengernum)
            print(passengername.name, passengername.passnum)
    elif user_input == '2':
        while True:
            plane = input('Name of plane ')
            planenum = input('Plane Number ')
            if plane == "" or planenum == "":
                print('Error, you failed to enter a key piece of information')
                continue
            else:
                plane = Planes(plane, planenum)
                print(plane.name, plane.planenum)
                break
    elif user_input == '3':
        flight = input('Whats your flight? ')
        while True:
            info = input(f'Do you want to add info to flight {flight}? (y/n)')
            if info == 'y':
                origin = input('What is the origin? ')
                destination = input('Where is it going? ')
                planenum = input('What is the plane number ')
                user_input = Flight(origin, destination, planenum)
                while True:
                    exit = input('Do you wish to add passnegers? (y/n) ')
                    if exit == 'y':
                        while True:
                            user_input = input('Name of passenger to add (or type exit to quit): ')
                            if user_input == 'exit':
                                print(passengers)
                                break
                            else:
                                passengers.append(user_input)
                    elif exit == 'n':
                        break
                    else:
                        print('Invalid response')
                        continue

            elif info == 'n':
                user_input = Flight()
            else:
                print('Invalid response')
                continue


    elif user_input == '4':
        break
    else:
        print('You didnt register a valid response')
        continue





