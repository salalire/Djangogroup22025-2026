from django.urls import path
from .import views 
urlpatterns = [
    path("home/",views.sayhello),
    path("cbf/", views.CBF.as_view(), name="cbf"),
    path("post/",views.fetch_posts),
]

