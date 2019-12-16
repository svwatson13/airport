from db_connect import *
import time

class Passengers(MSDBConnection):
    def add_passenger(self):
        first_name = input('What is the first name of this passenger ').strip()
        last_name = input('What is the last name of this passenger ').strip()
        passport_number = input('What is their passport number? ')
        query = f"INSERT into Passengers (first_name, last_name, passport_number)" \
                f" values ('{first_name}','{last_name}', '{passport_number}')"
        self._MSDBConnection__sql_query(query)
        self._MSDBConnection__sql_commit()
        print('Thank you for updating passenger info ')
        time.sleep(1)

    def change_passenger(self):
        query = f"SELECT * FROM Passengers"
        data = self._MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"ID({record.passenger_id}): {record.first_name} {record.last_name} - {record.passport_number}")
        ID = input('What is their passenger ID? ')
        change = input('\nWhat detail of this passenger would you like to change? '
                       '\n1) First name \n2) Second name \n3) First and Second name \n4) passport number \nChoose a number:  ')
        if change == '1':
            first_name = input('What is the new first name of this passenger ').strip()
            query = f"UPDATE Passengers set first_name = '{first_name}' where passenger_id like '{ID}'"
        if change == '2':
            last_name = input('What is the new last name of this passenger ').strip()
            query = f"UPDATE Passengers set first_name = '{last_name}' where passenger_id like '{ID}'"
        if change == '3':
            first_name = input('What is the new first name of this passenger ').strip()
            last_name = input('What is the new last name of this passenger ').strip()
            query = f"UPDATE Passengers set first_name = '{first_name}', last_name = '{last_name}' where passenger_id like '{ID}'"
        if change == '4':
            passport_number = input('What is their new passport number? ')
            query = f"UPDATE Passengers set passport_number = '{passport_number}' where passenger_id like '{ID}'"
        self._MSDBConnection__sql_query(query)
        self._MSDBConnection__sql_commit()
        print('Thank you for updating passenger info')
        time.sleep(1)




