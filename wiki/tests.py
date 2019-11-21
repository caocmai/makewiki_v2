# Create your tests here.
import unittest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from wiki.models import Page
from django.urls import reverse_lazy



# Convention is name of app and TestCase, this is a class go need to put class
# This to test for model
class WikiTestCase(TestCase):

    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True) # because assertEqual is something == to something, so T is equal to T
    
    def test_page_slugify_on_save(self):
        """ Test the slug generated when saving a Page. """

        # Author is required field in our model.
        # Create a user for this test, this creates a blank user, username is required for all sites
        # annonynous is user id = -1
        # user is here instead of in global class becuase you just want to use user here to test slugify
        user = User() # b/c User is a class
        user.save()

        # Creat and save Page to database.
        page = Page(title="My Test Page", content="test", author=user)
        page.save()

        self.assertEqual(page.slug, 'my-test-page')

# This test for view functions
class PageListViewTests(TestCase):
    """ This is test Integrations test, so testing multiple pages"""

    def test_multiple_pages(self):
        # Create a user for this test
        user = User.objects.create() # This line will both create the user and save it

        # Create a page and save
        Page.objects.create(title="My Testy Page", content="test", author=user)
        Page.objects.create(title="Another Test Page", content="test again", author=user)

        # Calling homepage and setting equal to response
        # make a Get request, self.clent is in TestCase
        response = self.client.get("")

        # Checks if page is ok so response with 200
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # Matches the number of pages we have in the database

        responses = response.context['pages']

        self.assertEqual(len(responses), 2)

        # Checks to make sure it's displayed in html
        self.assertQuerysetEqual(
            responses,
            ['<Page: My Testy Page>', '<Page: Another Test Page>'],
            ordered = False
        )

    def test_specific_page(self):
        # Create a user for this test
        user = User.objects.create() # This line will both create the user and save it

        # Create a page and save
        test_page = Page.objects.create(title="My Testy Page", content="test", author=user, slug='my-testy-page')
        # Page.objects.create(title="Another Test Page", content="test again", author=user)

        # Calling homepage and setting equal to response
        # make a Get request, self.clent is in TestCase

        response = self.client.get(reverse_lazy('wiki-details-page', args=(test_page.slug,)))

        # Checks if page is ok so response with 200
        self.assertEqual(response.status_code, 200)

    def test_create_wiki_page(self):
        """ Test so that the form page load when visiting create """
        response = self.client.get("/new_wiki/")

        self.assertEqual(response.status_code, 200)
 
 class FormPostTest(self):
     