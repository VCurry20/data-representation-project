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
    
    def getAll(self):
            cursor = self.getCursor()
            sql="select * from population"
            cursor.execute(sql)
            result = cursor.fetchall()
            self.closeAll()
            return result
            


    def findByID(self, id):
            cursor = self.getCursor()
            sql="select * from population where id = %s"
            values =(id, )

            cursor.execute(sql, values)
            result = cursor.fetchone()
            self.closeAll()
            return result
              
        
    def update(self, values):
            cursor = self.getCursor()
            # sql="insert into population (census_year, county_and_city, marital_status, sex, population) values (%s,%s,%s,%s,%s)"
            sql="update population set census_year= %s, county_and_city=%s marital_status= %s sex=%s population=%s where id = %s"
            #values = ("Joe", 22, 1)
            cursor.execute(sql, values)
            self.connection.commit()
            self.closeAll()

              

    def delete(self, id):
            cursor = self.getCursor()
            sql="delete from population where id = %s"
            values =(id, )
            cursor.execute(sql, values)
            self.connection.commit()
            self.closeAll()



populationDAO = PopulationDAO()