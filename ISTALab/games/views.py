from django.views import generic
from django.urls import reverse_lazy

from games.models import Game

class GamesListView(generic.ListView):
    model = Game
    template_name = 'games_list.html'
    context_object_name = 'games'

class GameDetailView(generic.DetailView):
    model = Game
    template_name = 'game_detail.html'
    context_object_name = 'game'

class GameCreateView(generic.edit.CreateView):
	model = Game
	template_name = 'game_new.html'
	fields = '__all__'

class GameEditView(generic.edit.UpdateView):
	model = Game
	fields = ['winner']
	template_name = 'game_edit.html'

class GameDeleteView(generic.edit.DeleteView):
	model = Game
	template_name = 'game_delete.html'
	success_url = reverse_lazy('games_list')