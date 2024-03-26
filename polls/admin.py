from django.contrib import admin
from .models import MultipleChoiceQuestion, Choice, FreeResponseQuestion, Response
# Register your models here.

admin.site.register([MultipleChoiceQuestion, Choice, FreeResponseQuestion, Response])
