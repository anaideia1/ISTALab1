from django.shortcuts import render

# Create your views here.
from django.views import generic

from games.models import Game

class HomePageView(generic.TemplateView):
	template_name = 'home.html'

class AboutPageView(generic.TemplateView):
	template_name = 'about.html'

class GamesListView(generic.ListView):
    '''
    class representing a list of all games
    '''
    model = Game
    template_name = 'games_list.html'
    context_object_name = 'games'


class GameDetailView(generic.DetailView):
    '''
    class representing detail info about a game
    '''
    model = Game
    template_name = 'game_detail.html'
    context_object_name = 'game'

