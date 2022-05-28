from django.test import TestCase
from django.test import TestCase

from .models import Location
# Create your tests here.

class LocationTestCLass(TestCase):
    #Set up Method
    def setUp(self):
        self.loc = Location(name="Africa")
        self.loc.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))

    def test_save_method(self):
        self.loc.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.loc.save_location()
        self.loc.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.loc.id)
        location.update_location('Juja')
        location = Location.get_location_id(self.loc.id)
        self.assertTrue(location.name == 'Juja')


