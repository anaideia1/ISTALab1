from django.db import models
from django.urls import reverse
from games.choices import ATTRIBUTE_CHOICES, SIDE_CHOICES

# Create your models here.

class Player(models.Model):
	nickname = models.CharField(max_length = 255)
	def __str__(self):
		return f'{self.nickname}'

class Hero(models.Model):
	name = models.CharField(primary_key=True, max_length = 255)
	attribute = models.SmallIntegerField(choices = ATTRIBUTE_CHOICES, default = 1)

	class Meta:
		verbose_name_plural = "Heroes"

class Group(models.Model):
	numMembers = models.SmallIntegerField()
	def __str__(self):
		return f'{self.id}'


class RelationsGroupHeroPlayer(models.Model):
	group = models.ForeignKey(Group, on_delete = models.CASCADE)
	hero = models.ForeignKey(Hero, on_delete = models.CASCADE)
	player = models.ForeignKey(Player, on_delete = models.CASCADE)
	networth = models.IntegerField()
	kda = models.FloatField()

class Team(models.Model):
	side = models.SmallIntegerField(choices = SIDE_CHOICES, default = 1) # false - radiant, true - dire
	kills = models.SmallIntegerField()
	player1 = models.ForeignKey(RelationsGroupHeroPlayer, on_delete = models.CASCADE, related_name='player1') 
	player2 = models.ForeignKey(RelationsGroupHeroPlayer, on_delete = models.CASCADE, related_name='player2') 

	def __str__(self):
		return 'team' + f'{self.id}'


class Game(models.Model):
	winner = models.SmallIntegerField(choices = SIDE_CHOICES, default = 1) # 1 - radiant, 2 - dire
	date = models.DateField(auto_now=False, auto_now_add=False)
	radiant = models.ForeignKey(Team, on_delete = models.CASCADE, related_name='radiant')
	dire = models.ForeignKey(Team, on_delete = models.CASCADE, related_name='dire')

	def __str__(self):
		return 'game' + f'{self.id}'

	def get_absolute_url(self):
		return reverse('game_detail', args=[str(self.id)])














