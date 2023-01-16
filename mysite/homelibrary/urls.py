from django.urls import path
from . import views

urlpatterns = [
    path('homelibrary/', include('homelibrary.urls')),
    path('', views.index, name='index'),
]