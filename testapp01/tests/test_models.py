from django.test import TestCase
from testapp01.models import Person as PersonModel

# models test
class Person(TestCase):
    def test_person_creation(self):
        person = PersonModel.objects.create(first_name="ABC", last_name="XYZ")
        self.assertTrue(isinstance(person, PersonModel))
        self.assertEqual(person.__unicode__(), person.first_name + ' ' + person.last_name)
