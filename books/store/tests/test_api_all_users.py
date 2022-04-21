import json

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse

from store.models import AllUsers
from store.serializers import AllUsersSerializer


class AllUsersApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.all_users_1 = AllUsers.objects.create(first_name='First', last_name='F', mail='1231da@daf.com',
                                                   password='123qwer')
        self.all_users_2 = AllUsers.objects.create(first_name='Second', last_name='S', mail='231da@daf.com',
                                                   password='123qwert')
        self.all_users_3 = AllUsers.objects.create(first_name='Third', last_name='T', mail='31da@daf.com',
                                                   password='123qwerty')

    def test_create(self):
        self.assertEqual(3, AllUsers.objects.all().count())
        url = reverse('allusers-list')

        data = {
            "first_name": "Ifpd",
            "last_name": 'Fds',
            "mail": "2das31da@daf.com",
            "password": '123'
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, AllUsers.objects.all().count())
        print(self.all_users_1)

    def test_get(self):
        """Тест на обращение к юзерам """
        url = reverse('allusers-list')
        response = self.client.get(url)
        serializer_data = AllUsersSerializer([self.all_users_1, self.all_users_2, self.all_users_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        # print(AllUsers.objects.last())
