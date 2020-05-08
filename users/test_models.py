from django.test import TestCase
from users.models import Cadet, Company

class CadetTestCase(TestCase):
    def setUp(self):
        co = Company.objects.create(shortname="A", longname="Alpha", regiment=1, motto="Spartans", mascot="Spartan")
        Cadet.objects.create(first="John", last="Doe", xnumber="x91111", company=co)
        Cadet.objects.create(first="Jane", last="Doe", xnumber="x92222", company=co)

    def test_cadets_(self):
        """All cadets should have an xnumber, first, and last name"""
        johndoe = Cadet.objects.get(xnumber="x91111")
        janedoe = Cadet.objects.get(xnumber="x92222")
        self.assertEqual(johndoe.name(), 'Doe, John')
        self.assertEqual(janedoe.name(), 'Doe, Jane')

