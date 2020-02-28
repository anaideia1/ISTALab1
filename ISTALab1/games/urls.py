from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('games/', views.GamesListView.as_view(), name="games-list"),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name="game-detail"),
    ]