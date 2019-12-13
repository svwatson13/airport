import pyodbc

class MSDBConnection():
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Airport'
        self.username = 'SA'
        self.password = 'Passw0rd2018'

        self.docker_Airport = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                               +self.server+';DATABASE='+self.database+';UID='+
                                               self.username+';PWD='+ self.password)

        self.cursor = self.docker_Airport.cursor()

    def __sql_query(self, sql_query):
        return self.cursor.execute(sql_query)
    def __sql_commit(self):
        return self.cursor.commit()

