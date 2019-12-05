from django.test import TestCase

# Create your tests here.


# class FormPostTest(TestCase):
#     """ To test form creation """

#     def test_form(self):

#         user = User.objects.create() # This line will both create the user and save it

#         form_info = {
#             'title': "Test title",
#             'content': "The content in here",
#             'author': user.id
#          }

#         # form = PageForm(data=form_info)
#         # self.assertTrue(form.is_valid())

#         response = self.client.post("/new_wiki/", form_info)
#         # 302 instead of 200 because when submitting it goes to the page as the slug, so basically redirects
#         self.assertEqual(response.status_code, 302)
