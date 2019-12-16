from db_passengers_oop import *
from db_flights_oop import  *
from db_planes_oop import *
import time

while True:
    time.sleep(1.0)
    user_input = input('\nPlease select an option: \n1) Passengers \n2) Flights \n3) Planes \n4) Exit \nChoose a number: ')
    if user_input == '1':
        while True:
            user_input1 = input('\nDo you wish to: \n1) Create a passenger \n2) Change passenger details \n3) Return to main menu \nChoose a number: ')
            if user_input1 == '1':
                Passengers().add_passenger()
            if user_input1 == '2':
                Passengers().change_passenger()
            elif user_input1 == '3':
                break
    if user_input == '2':
        while True:
            user_input2 = input('\nDo you wish to: \n1) List all flights \n2) List all flights in text file \n3) Create flight \n4) Add passengers to flight \n5) Return to main menu \nChoose a number: ')
            if user_input2 == '1':
                Flights().list_flights()
            elif user_input2 == '2':
                Flights().list_txt_flights()
            elif user_input2 == '3':
                Flights().add_flight()
            elif user_input2 == '4':
                Flights().add_passengers()
            elif user_input2 == '5':
                break
    if user_input == '3':
        while True:
            user_input3 = input('\nDo you wish to: \n1) List planes  \n2) Create plane \n3) Return to main menu \nChoose a number: ')
            if user_input3 == '1':
                Planes().list_planes()
            elif user_input3 == '2':
                Planes().add_plane()
            elif user_input3 == '3':
                break
    if user_input == '4':
        break
    else:
        continue






