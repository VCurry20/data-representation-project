# put all the individual SQL command python scripts into one
# use functions to store the scripts

import mysql.connector
# sql="insert into population (census_year, county_and_city, marital_status, sex, population) values (%s,%s,%s,%s,%s)"

import config as cfg

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

    
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    def create(self, values):
        cursor = self.getCursor()
        sql="insert into population (census_year, county_and_city, marital_status, sex, population) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid


populationDAO = PopulationDAO()