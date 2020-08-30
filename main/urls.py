from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('predictMPG', views.predictMPG, name = 'predictMPG'),
    path('viewDataBase', views.viewDatabase,name='viewDatabase'),
    path('updateDataBase', views.updateDataBase,name='updateDataBase'),
]
