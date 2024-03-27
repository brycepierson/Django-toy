from .models import Monster
from django.templatetags.static import static
# module for managing the directory of images for the monsters

imageDirPath = static("dungeonsanddragons/monsterImages/")
def validateMonsterImageDirectory():
    return imageDirPath

def updateMonsterImageDirectory():
    return imageDirPath

def deleteMonsterImageDirectory():
    return imageDirPath
