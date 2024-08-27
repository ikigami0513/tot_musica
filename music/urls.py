from django.urls import path
from . import views

urlpatterns = [
    path('musics/', views.MusicListView.as_view(), name='musics_list_view'),
    path('music/', views.RetrieveMusicView.as_view(), name='retrieve_music_data'),
]
