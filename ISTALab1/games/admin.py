from django.contrib import admin

# Register your models here.

from .models import Game, Team, Group, Player, Hero, RelationsGroupHeroPlayer

admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Group)
admin.site.register(Player)
admin.site.register(Hero)
admin.site.register(RelationsGroupHeroPlayer)