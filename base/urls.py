from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationView.as_view(), name='application_view'),
    path('index/', views.IndexView.as_view(), name='index_view')
]
