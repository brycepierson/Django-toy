from .models import Monster
from django.templatetags.static import static
import os
# module for managing the directory of images for the monsters

imageDirPath = static("dungeonsanddragons/monsterImages/")

def validateMonsterImageDirectory():
    if not os.path.exists(imageDirPath):
        return False, "Directory does not exist"
    
    if not existsDirForEachMonster():
        return False, "Each monster doesn't have their own directory"

    return True, ""

def updateMonsterImageDirectory():
    os.makedirs(imageDirPath, exist_ok=True)

    for monster in Monster.objects.all():
        os.mkdir(os.path.join(imageDirPath, monster.id))
    return 

def deleteMonsterImageDirectory():
    return imageDirPath

def existsDirForEachMonster():
    for monster in Monster.objects.all():
        if not os.path.exists(os.path.join(imageDirPath, monster.id)):
            return False
    return True