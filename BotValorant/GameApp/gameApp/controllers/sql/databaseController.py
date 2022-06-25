import pyodbc
from GameApp.gameApp.controllers.dataBaseController import dataBase

class dataBaseController:
    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};Server=DELKEIS_DESKTOP;Database=ProjetA;Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    def extractDb(self):
        self.cursor.execute('SELECT * FROM player')
        tmpDb = dataBase()
        for item in self.cursor:
            if tmpDb.searchData(item['discordId']) == True:
                print("entrée trouver")
            else:
                print("entrée non trouver") 


db = dataBaseController()
db.extractDb()



#try:
#    conn = pyodbc.connect('Driver={SQL Server};Server=DELKEIS_DESKTOP;Database=ProjetA;Trusted_Connection=yes;')
#except:
#    print("mauvais arguments !")
#    exit()

#cursor = conn.cursor()


#cursor.execute('''INSERT INTO player
#                  VALUES (?, ?, ?, ?, ?, ?, ?)''', 
#                (id, name, lvl, xp, did, rid, puuid))
#cursor.execute('SELECT * FROM player')

#for i in cursor:
#    print(i)

