from django.test import TestCase
from waste_segregation_app.models import Trash

class TrashTestCase(TestCase):
    def setUp(self):
        Trash.objects.create(trash_description="plastic bag")
        Trash.objects.create(trash_description="paper")

    def test_check_bin(self):
        plastic_bag= Trash.objects.get(trash_description="plastic bag")
        paper = Trash.objects.get(trash_description="paper")
        self.assertEqual(plastic_bag.check_bin(), 'yellow')
        self.assertEqual(paper.check_bin(), 'blue')
