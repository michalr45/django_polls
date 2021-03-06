from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.create_poll, name='create_poll'),
    path('poll/<slug:slug>/', views.poll_detail, name='poll_detail'),
    path('poll/<slug:slug>/vote', views.poll_vote, name='poll_vote'),
    path('poll/<slug:slug>/results', views.poll_results, name='poll_results'),
    path('polls/dashboard', views.polls_dashboard, name='polls_dashboard'),
    path('poll/<slug:slug>/delete', views.delete_poll, name='delete_poll'),
]
