from django.urls import path
from rehearsal_website import views

urlpatterns = [
    path('', views.mainPage, name='rehearsal_website'),
    path('play/', views.submit, name='play')
]
