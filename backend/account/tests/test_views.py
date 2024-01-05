from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class RegisterAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_register_user_with_valid_data(self):
        data = {
            "username": "john123",
            "email": "johndoe@example.com",
            "password": "secret",
        }
        url = "/auth/reg/"
        want = {"status": "good", "user_id": 1}

        get = self.client.post(url, data, format="json")

        # get resp success
        self.assertEqual(200, get.status_code)
        self.assertEqual(want, get.data)

        # user is created?
        user = User.objects.get(username=data["username"])
        self.assertIsNotNone(user)

        # get on resp real user_id created user
        self.assertEqual(want["user_id"], user.id)

    def test_register_user_without_email(self):
        data = {
            "username": "john123",
            "password": "secret",
        }
        url = "/auth/reg/"
        want = {"status": "bad"}

        get = self.client.post(url, data, format="json")

        self.assertEqual(want, get.data)

        # user is created?
        user = User.objects.filter(username=data["username"]).first()
        self.assertIsNone(user)

    def test_register_user_without_username(self):
        data = {
            "email": "we@dfd.ru",
            "password": "secret",
        }
        url = "/auth/reg/"
        want = {"status": "bad"}

        get = self.client.post(url, data, format="json")

        self.assertEqual(want, get.data)

    def test_register_user_without_password(self):
        data = {
            "username": "john123",
            "email": "we@dfd.ru",
        }
        url = "/auth/reg/"
        want = {"status": "bad"}

        get = self.client.post(url, data, format="json")

        self.assertEqual(want, get.data)

        # user is created?
        user = User.objects.filter(username=data["username"]).first()
        self.assertIsNone(user)
