from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('create_poll/', views.create_poll, name='create_poll')
]