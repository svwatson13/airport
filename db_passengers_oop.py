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




