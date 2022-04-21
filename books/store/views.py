from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from store.models import Book, AllUsers
from store.permissions import IsOwnerOrStaffOrReadOnly
from store.serializers import BooksSerializer, AllUsersSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class AllUsersViewSet(ModelViewSet):
    queryset = AllUsers.objects.all()
    serializer_class = AllUsersSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    search_fields = ['first_name', 'last_name']


def all_users(request):
    return render(request, 'all_users.html', {'users': AllUsers.objects.all()})


def auth(request):
    return render(request, 'oauth.html')


def blog(request):
    return render(request, 'blog.html')
