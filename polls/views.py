from rest_framework.views import APIView
from .serializers import NoteSerializer
from .models import Note
from rest_framework.response import Response
from rest_framework import status

class NoteList(APIView):
    def get(self, request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Note.objects.using('default').get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)