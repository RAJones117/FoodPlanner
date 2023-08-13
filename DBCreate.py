# Database Creation

import sqlite3
from sqlite3 import Error
import csv
import pandas as pd

def create_connection(db_file):

    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

create_connection(r"./pythonsqlite.db")


impConn = sqlite3.connect(r"./pythonsqlite.db")
c = impConn.cursor()
createTable = 'CREATE TABLE IF NOT EXISTS Recipes([Recipe] TEXT, [Ingredient] TEXT, [Amount] REAL, [Unit] TEXT)'

c.execute(createTable)
c.execute('DELETE FROM RECIPES')

with open(r'./RawData.csv','r') as f:
    reader = csv.reader(f, dialect='excel')
    next(reader)
    for row in reader:
        insSql = 'INSERT INTO Recipes (Recipe, Ingredient, Amount, Unit) Values (\''+row[0]+'\',\''+row[1]+'\','+str(row[2])+',\''+row[3]+'\')'
        c.execute(insSql)


impConn.commit()
impConn.close()

newCon = sqlite3.connect(r"./pythonsqlite.db")
df = pd.read_sql_query('SELECT * FROM RECIPES', newCon)

print(df)

newCon.close()

