from django.test import TestCase


class TestAccessPerms(TestCase):
    def test_no_perms(self):
        self.assertTrue(True)

    # def test_perms(self):
    #     self.assertTrue(False)
