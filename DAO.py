# put all the individual SQL command python scripts into one
# use functions to store the scripts

# import SQL Connector
import mysql.connector

# import config file
import config as cfg

# set class
class PopulationDAO:
    connection = ""
    cursor =''
    host =''
    user = ''
    password =''
    database =''



    def __init__(self): 
        #these should be read from a config file
        self.host=   cfg.mysql['host']
        self.user=   cfg.mysql['user']
        self.password= cfg.mysql['password']
        self.database= cfg.mysql['database']

    # define connection
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    # define close connection
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    # define create
    def create(self, values):
        cursor = self.getCursor()
        sql="insert into population (id,census_year, county_and_city, marital_status, sex, population) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    # define get all
    def getAll(self):
            cursor = self.getCursor()
            sql="select * from population"
            cursor.execute(sql)
            result = cursor.fetchall()
            self.closeAll()
            return result
            

    # define get by id
    def findByID(self, id):
            cursor = self.getCursor()
            sql="select * from population where id = %s"
            values =(id, )

            cursor.execute(sql, values)
            result = cursor.fetchone()
            self.closeAll()
            return result
              

    # define update   
    def update(self, values):
            cursor = self.getCursor()
            sql="update population set census_year= %s, county_and_city=%s marital_status= %s sex=%s population=%s where id = %s"

            cursor.execute(sql, values)
            self.connection.commit()
            self.closeAll()


    # define delete
    def delete(self, id):
            cursor = self.getCursor()
            sql="delete from population where id = %s"
            values =(id, )
            cursor.execute(sql, values)
            self.connection.commit()
            self.closeAll()



populationDAO = PopulationDAO()