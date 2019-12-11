import pyodbc

server = 'localhost,1433'
database = 'Airport'
username = 'SA'
password = 'Passw0rd2018'

docker_Airport = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = docker_Airport.cursor()

cursor.execute("SELECT * FROM Flights")

# Fetching data from the executed SQL command and printing
row = cursor.fetchone()
print(row)
print(row.flight_name)
print(row.plane_number)

## Iterate over table and print specified details
# rows_all = cursor.fetchall()
# for row in rows_all:
#     print(row.flight_name, '-', row.plane_number)

# # To get lots of data - use a while loop and fetchone at a time
rows = cursor.execute("SELECT * FROM Flights")
while True:
    record = rows.fetchone()
    if record is None:
        break
    else:
        print(record.flight_name)

