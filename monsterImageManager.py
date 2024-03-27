import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

class monsterImageManager():
    def __init__(self):
        dbFileURL = "db.sqlite3"
        monsterTable = "dungeonsanddragons_monster"

        db = sqlite3.connect(dbFileURL)
        cursor = db.cursor()
        query = "select * from " + monsterTable + ";"
        self.monsters = cursor.execute(query)
    
    def findImage(self, monster):
        pass
        
    def populateMonsterImages(self):

        for monster in self.monsters:

            print(monster.keys)


if __name__ == "__main__":
    mim = monsterImageManager()
    mim.populateMonsterImages()