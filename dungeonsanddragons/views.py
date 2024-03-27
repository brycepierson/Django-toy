from django.shortcuts import render, get_object_or_404
from .models import Monster
from django.conf import settings
from .monsterImages import validateMonsterImageDirectory, deleteMonsterImageDirectory, updateMonsterImageDirectory, imageDirPath
# Create your views here.

def index(request):
    apikey = settings.API_KEY
    isValid, error = validateMonsterImageDirectory()
    if not isValid:
        updateMonsterImageDirectory()
    return render(request, "dungeonsanddragons/index.html", {"apikey": apikey,})

def question(request):
    return render(request, "dungeonsanddragons/question.html", {})

def detail(request, monster_id):
    monster = get_object_or_404(Monster, pk=monster_id)
    return render(request, "dungeonsanddragons/detail.html", {"monster": monster, "monsterImgURL": imageDirPath})
