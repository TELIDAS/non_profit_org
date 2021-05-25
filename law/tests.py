from django.test import TestCase, Client

# Create your tests here.
from law.models import Law


class TestLaw(TestCase):

    def test_create_model_law(self):
        title = 'title'
        description = 'description'
        laws = Law.objects.create(title=title, description=description)
        self.assertEquals(laws.title, title)
        self.assertEquals(laws.description, description)
