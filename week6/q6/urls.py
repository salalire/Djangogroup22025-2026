from django.urls import path
from .views import book_list,books_never_loaned,science_books_by_newton,top_members,books_per_category

urlpatterns = [
    path("books/", book_list),
    path("books/never-loaned/", books_never_loaned),
    path("books/science-newton/", science_books_by_newton),
    path("members/top/", top_members),
    path("categories/count/", books_per_category),
]
