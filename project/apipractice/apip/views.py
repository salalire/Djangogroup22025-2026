from django.shortcuts import render
from django.http import JsonResponse
from .models import Note
import json
from django.views.decorators.csrf import csrf_exempt
def note_list(request):
    notes=Note.objects.all().values("id","title","messages")
    data=list(notes)
    return JsonResponse(data,safe=False)
@csrf_exempt
def create_note(request):
    if request.method=="POST":
        data=json.loads(request.body)
        note=Note.objects.create(
            title=data["title"],
            messages=data["messages"]
        
        )
        return JsonResponse(
        {
            "id":note.id,
            "messages":"note.created"
            
        }
    )
def update_note(request,note_id):
    if request.method=="PUT":
        data=json.loads(request.body)
        try:
            note=Note.objects.get(id=note_id)
            note.title=data["title"]
            note.messages=data["messages"]
            note.save()
            return JsonResponse(
                {
                    "id":note.id,
                    "messages":"note.updated"
                }
            )
        except Note.DoesNotExist:
            return JsonResponse(
                {
                    "messages":"note.not.found"
                },
                status=404
            )

def delete_note(request,note_id):
     if request.method != "DELETE":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )
     try:
            note=Note.objects.get(id=note_id)
            note.delete()
            return JsonResponse(
                {
                    "id":note_id,
                    "message":"note deleted"
                }
            )
     except Note.DoesNotExist:
            return JsonResponse(
                {
                    "message":"Not is not found"
                },
                status=404
            )
            
