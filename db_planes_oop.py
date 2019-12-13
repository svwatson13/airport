from db_connect import *
import time
class Planes(MSDBConnection):
    def add_plane(self):
        plane_name = input('What is the planes name ').strip()
        plane_number = input('What is the planes number? ').strip()
        query = f"INSERT into Planes (plane_name, plane_number)" \
                f" values ('{plane_name}','{plane_number}')"
        try:
            self._MSDBConnection__sql_query(query)
            self._MSDBConnection__sql_commit()
        except pyodbc.IntegrityError as error:
            print('This plane has already been created')
        finally:
            print('Thank you')


    def list_planes(self):
        query = f"SELECT * FROM Planes"
        data = self._MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"\nPlane: {record.plane_name}: {record.plane_number}")
            time.sleep(0.2)