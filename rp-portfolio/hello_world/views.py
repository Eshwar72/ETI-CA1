from django.shortcuts import render
from django.urls import path
from hello_world import views

# Create your views here.
def hello_world(request):
    return render(request, 'hello_world.html', {})

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
