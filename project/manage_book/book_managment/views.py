from django.shortcuts import render
from django.http import JsonResponse
from .models import Book,Author
from django.views.decorators.csrf import csrf_exempt
import json

def display_books(request):
    if request.method!="GET":
        return JsonResponse({
            "Error":"method not matched" 
            
        },
        staus=405
        )
    books=Book.objects.all().values('title','author','published_date','isbn')
    data=list(books)
    return JsonResponse(data,safe=False)
def get_one_book(request,book_id):
    if request.method!="GET":
        return JsonResponse({
            "Error":"mthod not matched "
            
        },
        staus=405
        )
    try:
        book=Book.objects.get(id=book_id)
        data={
            "title":book.title,
            "author":book.author.name,
            "published_date":book.published_date,
            "isbn":book.isbn
        }
        return JsonResponse(data)
    except Book.DoesNotExist:
        return JsonResponse({
            "Error":"book not found"
        },
        status=404
        )
@csrf_exempt
def create_book(request):
    if request.method!="POST":
        return JsonResponse({
            "Error":"method not matched"
        },
        status=405
        )
    try:
        data=json.loads(request.body)
        book=Book.objects.create(
            title=data["title"],
            author=Author.objects.get(id=data["author_id"]),
            published_date=data["published_date"],
            isbn=data["isbn"]
        )
        return JsonResponse({
            "id":book.id,
            "message":"book created"
        },
        status=201
        )
    except Author.DoesNotExist:
        return JsonResponse({
            "Error":"author not found"
        },
        status=404
        )
        
@csrf_exempt       
def update_book(request,book_id):
    if request.method!="PUT":
        return JsonResponse({
            "Error":"method not matched"
        },
        status=405
        )
    try:
        data=json.loads(request.body)
        book=Book.objects.get(id=book_id)
        book.title=data["title"]
        book.author=Author.objects.get(id=data["author_id"])
        book.published_date=data["published_date"]
        book.isbn=data["isbn"]
        book.save()
        return JsonResponse({
            "id":book_id,
            "message":"book updated"
        },
        status=201
        )
    except Author.DoesNotExist:
        return JsonResponse({
            "Error":"author not found"
        },
        status=404
        )
@csrf_exempt       
def delete_book(request,book_id):
    if request.method!="DELETE":
        return JsonResponse(
            {
                "message":"method is not allowed "
            },
            status=405
        )
    try:
        book=Book.objects.get(id=book_id)
        book.delete()
        return JsonResponse(
            {
                "message":"book deleted successfully"
            },
            status=203
        )
    except Book.DoesNotExist:
        return JsonResponse(
            {
                "Error":"Book does not exist"  
            },
            status=404
        )