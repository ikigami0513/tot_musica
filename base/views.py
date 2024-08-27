from django.shortcuts import render
from django.http import HttpRequest
from django.views import View

class ApplicationView(View):
    def get(self, request: HttpRequest):
        return render(request, 'layout.html')
    
class IndexView(View):
    def get(self, request: HttpRequest):
        return render(request, 'index.html')
    