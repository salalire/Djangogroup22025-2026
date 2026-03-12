from django.urls import path
from . import views
urlpatterns = [
    path('lobby/', views.lobby, name='lobby'),
    path('member_lounge/', views.member_lounge, name='member_lounge'),
    path('managers/', views.manager_office, name='manager_office')
]