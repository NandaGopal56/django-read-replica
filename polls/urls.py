from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NoteList.as_view(), name='get-all-notes'),
    path('note/<pk>', views.NoteList.as_view(), name='get-a-note'),
    path('note/create', views.NoteList.as_view(), name='create-a-note'),
    path('note/delete/<pk>', views.NoteList.as_view(), name='delete-a-note'),
]