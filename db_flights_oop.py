from db_connect import *
import time

class Flights(MSDBConnection):
    def add_flight(self):
        flight_name = input('What is the flight name ').strip()
        origin = input('What is the flights origin? ').strip()
        destination = input('What is the destination of this flight? ').strip()
        while True:
            plane_number = input('What is the plane number for this flight ')
            query1 = "SELECT plane_number FROM Planes"
            data1 = self._MSDBConnection__sql_query(query1)
            planes = []
            for i in data1.fetchall():
                a = (i[0])
                planes.append(a)
            if plane_number in planes:
                query1 = f"INSERT into Flights (flight_name, plane_number, origin, destination) " \
                         f"values ('{flight_name}', '{plane_number}', '{origin}', '{destination}')"
                self._MSDBConnection__sql_query(query1)
                self._MSDBConnection__sql_commit()
                print('Thank you for updating passenger info ')
                time.sleep(1)
                break
            else:
                print('That is not a valid plane_number')
                continue

    def list_flights(self):
        query = f"SELECT * FROM Flights"
        data = self._MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"\nID{record.flight_id}: {record.flight_name} \nPlane Number: {record.plane_number}"
                  f"\nFlights Details: {record.origin} --> {record.destination}\n")
            time.sleep(1)

    def list_txt_flights(self):
        query = f"SELECT * FROM Flights"
        data = self._MSDBConnection__sql_query(query)
        with open("Flights.txt", 'w+') as file_to_read:
            while True:
                record = data.fetchone()
                if record is None:
                    break
                file_to_read.write(f"\nID{record.flight_id}: {record.flight_name} \nPlane Number: {record.plane_number} \nFlights Details: {record.origin} --> {record.destination}\n")

    def add_passengers(self):
        passport_number = input('What is their passport number? ').strip()
        while True:
            flight_id = int(input(('What is the flight ID you wish to add to this passenger? ')))
            query = "SELECT flight_id from Flights"
            data = self._MSDBConnection__sql_query(query)
            flights = []
            for i in data.fetchall():
                a = (i[0])
                flights.append(a)
            if flight_id in flights:
                query1 = f"UPDATE Passengers set flight_id = {flight_id} where passport_number like '{passport_number}'"
                self._MSDBConnection__sql_query(query1)
                self._MSDBConnection__sql_commit()
                print('Thank you for updating flight info ')
                time.sleep(1)
                break
            else:
                print('That is not a valid flight_id')
                continue

