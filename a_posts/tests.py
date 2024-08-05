from django.test import TestCase
from django.urls import reverse


class SignUpTest(TestCase):
    def test_sign_up_page_exists(self):
        response = self.client.get(reverse("account_signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signup.html")

    def test_sign_up_user(self):
        user_data = {
            "email": "test@email.com",
            "username": "testuser",
            "password1": "password1",
            "password2": "password2",
        }

        response = self.client.post(reverse("account_signup"), user_data, format="text/html")
        self.assertEqual(response.status_code, 200)

    #     response = self.client.get(
    #         reverse("user-profile", args=[user_data["username"]])
    #     )
    #     self.assertEqual(response.status_code, 404)


# class BaseSetup(TestCase):

#     def setUp(self):
#         user_data = {
#             "email": "test@email.com",
#             "username": "testuser",
#             "password1": "password1",
#             "password2": "password2",
#         }

#         self.client.post(reverse("account_signup"), user_data, format="text/html")


# class ProfileEditTest(BaseSetup):

#     def test_profile_edit(self):
#         # self.client.logout()
#         response = self.client.get(reverse("profile-edit"))
#         self.assertEqual(response.status_code, 200)
