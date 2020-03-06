from django.urls import path

from . import views

urlpatterns = [
    path('', views.GamesListView.as_view(), name="games_list"),
    path('<int:pk>/', views.GameDetailView.as_view(), name="game_detail"),
    path('new/', views.GameCreateView.as_view(), name="game_new"),
    path('<int:pk>/edit/', views.GameEditView.as_view(), name="game_edit"),
    path('<int:pk>/delete/', views.GameDeleteView.as_view(), name="game_delete"),
    ]