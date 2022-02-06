from dictionary.models import Words
from rest_framework import viewsets, permissions
from .serializers import WordSerializer

#Word ViewSet
class WordViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    serializer_class = WordSerializer
    
    def get_queryset(self):
        return self.request.user.wordlist.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

'''
    queryset = Words.objects.all()
    permissions = [
        permissions.AllowAny        
    ]
    serializer_class = WordSerializer

'''
   

