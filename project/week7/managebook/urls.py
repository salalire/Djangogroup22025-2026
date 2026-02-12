from django.urls import path,include
from . import views
urlpatterns = [
   path("book-after-2010/",views.book_after_2010),
   path("book-with-title-python/",views.book_with_title_python) ,
   path ("usa-author/",views.usa_author),
   path("book-with-author/",views.book_with_name),
   path("author-with-book/",views.author_with_title),
   path("not-free-books/",views.not_free_book),
   path("higher-author/",views.authors_with_hgher_price),
]
