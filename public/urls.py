from django.urls import path

from . import views

app_name = 'public'
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginRoute, name='login'),
    path('ready/', views.index, name='ready'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),

]
