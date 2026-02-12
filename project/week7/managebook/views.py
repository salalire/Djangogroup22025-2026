from django.shortcuts import render
from .models import Book,Author
from django.http import HttpResponse
from django.db.models import Sum

def book_after_2010(request):
    books = Book.objects.filter(published_year__gt=2010)

    result = ""
    for b in books:
        result += f"Title: {b.title}, Published Year: {b.published_year}<br>"

    return HttpResponse(result)

def book_with_title_python(request):
    books=Book.objects.filter(title__icontains="python")
    result = ""
    for b in books:
        result += f"Title: {b.title}<br>"

    return HttpResponse(result)

def usa_author(request):
    authors=Author.objects.filter(country__iexact="usa").order_by("name")
    result="" 
    for a in authors:
        result+=f"Name: {a.name}, Country: {a.country}<br>"
    return HttpResponse(result)
def book_with_name(request):
    book_author=Book.objects.select_related("author")
    result=""
    for ba in book_author:
        result+=f"Book: {ba.title}, Author: {ba.author.name}<br>"
    return HttpResponse(result)  
def author_with_title(request):
    author_book=Author.objects.prefetch_related("books") 
    result=""
    for ab in author_book:
        result+=f"Author: {ab.name}<br>" 
        for book in ab.books.all():
            result+=f"Book_Title: {book.title} <br>"
    return HttpResponse(result)
def not_free_book(request):
    not_free_books=Book.objects.filter(price__gt=0,isbn__regex=r'^\d{13}$')
    result=""
    for book in not_free_books:
        result+=f"Title: {book.title} <br>" 
    return HttpResponse(result)

def authors_with_hgher_price(request):
    higher_authors=Author.objects.filter(books__price__gt=50).distinct().prefetch_related("books")
    result=""
    for author in higher_authors:
        result+=f"Author: {author.name} <br>"
        for book in author.books.all():
            result+=f"Book title: {book.title}  Price: {book.price}<br>"
        result+="<br>"    
    return HttpResponse(result)

def top5_authors(request):
    top5_authors=Author.objects.annotate(total_revenue=Sum("books__price")).order_by("-total_revenue")[:5]
    result=""
    for author in top5_authors:
        result+=f"Author: {author.name}  Total Revenue: {author.total_revenue}<br>"
    return HttpResponse(result)
    