import mysql.connector

import config as cfg

mydb = mysql.connector.connect(
    host= cfg.mysql['host'],
    user= cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database'],
)


mycursor = mydb.cursor()

sql="CREATE TABLE population (id INT AUTO_INCREMENT PRIMARY KEY, census_year VARCHAR(250), county_and_city VARCHAR(250), marital_status VARCHAR(250), sex VARCHAR(250), population INT)"


mycursor.execute(sql)

mydb.close()
mycursor.close()