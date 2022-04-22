from rest_framework.serializers import ModelSerializer

from store.models import Book, AllUsers, UserBookRelation


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AllUsersSerializer(ModelSerializer):
    class Meta:
        model = AllUsers
        fields = '__all__'


class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')
