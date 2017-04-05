from django.contrib import admin
from .models import team, players, club_history


# Register your models here.
admin.site.register(team)
admin.site.register(players)
admin.site.register(club_history)


