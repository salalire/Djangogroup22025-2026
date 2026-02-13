from django.urls import path
from . import views
urlpatterns=[
    path("list/",views.note_list,name="note-list"),
    path("create/",views.create_note,name="create-note"),
    path("<int:note_id>/update/",views.update_note),
    path("<int:note_id>/delete/",views.delete_note),
]