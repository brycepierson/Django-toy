from django.shortcuts import render, get_object_or_404
from .models import Monster
# Create your views here.

def index(request):
    pass



def detail(request, monster_id):
    question = get_object_or_404(Monster, pk=monster_id)
    return render(request, "polls/detail.html", {"question": question})
