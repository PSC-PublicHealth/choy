from django.urls import path

from deepseaweb.views import index

urlpatterns = [
    path('', index, name='index'),
   
]
