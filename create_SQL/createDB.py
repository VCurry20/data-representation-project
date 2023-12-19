import mysql.connector

import config as cfg

db = mysql.connector.connect(
    host= cfg.mysql['host'],
    user= cfg.mysql['user'],
    password=cfg.mysql['password'],
)

cursor = db.cursor()

cursor.execute("create DATABASE project_SQL")

db.close()
cursor.close()