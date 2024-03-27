import sqlite3
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

class monsterImageManager():
    def __init__(self):
        load_dotenv()

        dbFileURL = "db.sqlite3"
        monsterTable = "dungeonsanddragons_monster"
        static_folder = "./dungeonsanddragons/static/dungeonsanddragons/"
        self.image_folder = os.path.join(static_folder, "monsterImages/")
        connection = sqlite3.connect(dbFileURL)
        connection.row_factory = sqlite3.Row
        query = "select * from " + monsterTable + ";"
        self.monsters = connection.execute(query)
        self.service = build(
            "customsearch", "v1", developerKey=os.environ.get('IMAGE_API_KEY')
        )
    def findImageLinks(self, monster, number):
        res = (
            self.service.cse()
            .list(
                q=monster['name'],
                cx=os.environ.get('CSE_ID'),
                imgSize='LARGE',
                searchType='image',
                num=number,
            )
            .execute()
        )
        items = res.get('items')
        links = [item.get('link') for item in items]
        return links
    
    def downloadImages(links, directory):
        #download the images in the links to the given directory
        pass
    def populateMonsterImages(self):

        for monster in self.monsters:
            monster_folder = os.path.join(self.image_folder, str(monster['id']))
            # see if there are 5 images
            
            # Get 5 images

            print(monster_folder)


if __name__ == "__main__":
    mim = monsterImageManager()
    print(mim.findImageLinks(mim.monsters.fetchone(), 10))

    #mim.populateMonsterImages()