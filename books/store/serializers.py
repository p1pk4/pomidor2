from rest_framework.serializers import ModelSerializer

from store.models import Book, AllUsers


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AllUsersSerializer(ModelSerializer):
    class Meta:
        model = AllUsers
        fields = '__all__'
