from django.contrib import admin

from .models import Question, Choix

admin.site.register(Question)
admin.site.register(Choix)
