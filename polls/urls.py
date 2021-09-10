from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('create_poll/', views.create_poll, name='create_poll'),
    path('poll/<slug:slug>/', views.poll_detail, name='poll_detail'),
    path('poll/<slug:slug>/vote', views.poll_vote, name='poll_vote'),
    path('poll/<slug:slug>/results', views.poll_results, name='poll_results')
]
