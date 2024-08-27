from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views import View

from .serializers import MusicSerializer
from .models import Music

class MusicListView(View):
    def get(self, request: HttpRequest):
        musics = Music.objects.all()
        return render(request, 'music/list.html', context={
            'musics': musics
        })
    
class RetrieveMusicView(View):
    def get(self, request: HttpRequest):
        id = request.GET.get('id')
        if id is None:
            return JsonResponse({
                "success": False,
                "message": "Id no provided"
            })
        
        try:
            music = Music.objects.get(id=id)
        except Music.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Music not found"
            })
        
        serialize = MusicSerializer(music)
        return JsonResponse({
            "success": True,
            "music": serialize.data
        })
