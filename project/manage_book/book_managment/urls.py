from django.urls import path
from . import views
urlpatterns=[
    path("list/",views.display_books), 
    path("<int:book_id>/",views.get_one_book), 
    path("create/",views.create_book),
]