from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('signin',views.signin, name='signin'),
    path('Dog',views.Dog, name='Dog'),
    path('login',views.login, name='login'),
    path('Cat',views.Cat, name='Cat'),
    path('aquatic',views.aquatic, name='aquatic'),
    path('cssLogin',views.cssLogin, name='cssLogin'),
]