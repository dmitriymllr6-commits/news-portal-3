from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filterset_fields = ['author']
    ordering_fields = ['date_created']
    ordering = ['-date_created']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)